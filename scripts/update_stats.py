import os
import json
import sys
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange, Dimension, Metric, RunReportRequest, OrderBy, FilterExpression, Filter
)
from datetime import datetime, timedelta

PROPERTY_ID = os.environ.get("GA_PROPERTY_ID")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

if not PROPERTY_ID:
    print("Error: GA_PROPERTY_ID is missing.")
    sys.exit(1)

client = BetaAnalyticsDataClient()

def get_daily_data(days, page_path=None):
    """최근 N일간의 데이터를 1일 단위로 추출 (데이터가 없으면 0으로 채움)"""
    # 1. 기준 날짜 리스트 생성 (어제부터 역산)
    yesterday = datetime.now() - timedelta(days=1)
    date_list = [(yesterday - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(days)]
    # { "2026-03-24": 0, "2026-03-23": 0 ... } 초기화
    results_dict = {date: 0 for date in date_list}

    # 2. GA4 API 호출
    dim_filter = None
    if page_path:
        dim_filter = FilterExpression(filter=Filter(field_name="pagePath", 
            string_filter=Filter.StringFilter(match_type=Filter.StringFilter.MatchType.BEGINS_WITH, value=page_path)))

    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[Dimension(name="date")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date=f"{days}daysAgo", end_date="yesterday")],
        dimension_filter=dim_filter
    )
    
    response = client.run_report(request)

    # 3. API 응답 데이터를 결과 딕셔너리에 매칭
    for row in response.rows:
        raw_date = row.dimension_values[0].value # YYYYMMDD
        formatted_date = f"{raw_date[:4]}-{raw_date[4:6]}-{raw_date[6:]}"
        if formatted_date in results_dict:
            results_dict[formatted_date] = int(row.metric_values[0].value)

    # 4. 날짜순으로 정렬하여 반환
    return [{"date": k, "value": v} for k, v in sorted(results_dict.items())]


def get_monthly_data(months, page_path=None):
    """최근 N개월간의 데이터를 1달 단위로 추출 (데이터가 없으면 0으로 채움)"""
    # 1. 기준 월 리스트 생성 (이번 달 포함 최근 N개월)
    now = datetime.now()
    month_list = []
    for i in range(months):
        # 월 계산 (연도가 바뀌는 경우 포함)
        target_date = now.replace(day=1) - timedelta(days=i*30) # 대략적인 월 계산 후 보정
        # 정확한 월 리스트를 위해 연/월 문자열 생성
        m_str = (datetime(now.year, now.month, 1) - timedelta(days=1 if now.month == 1 else 0)).replace(day=1) # 로직 단순화
        # 실제로는 아래와 같이 반복문 안에서 각 월의 첫날을 기준으로 계산하는 것이 정확합니다.
        dt = (now.replace(day=1) - timedelta(days=1)).replace(day=1) # 지난달부터 시작할 경우
        # 단순 반복문으로 YYYY-MM 생성
    
    # 더 직관적인 월 생성 로직
    results_dict = {}
    curr_date = now
    for _ in range(months):
        m_key = curr_date.strftime('%Y-%m')
        results_dict[m_key] = 0
        # 이전 달로 이동
        curr_date = (curr_date.replace(day=1) - timedelta(days=1))

    # 2. GA4 API 호출
    dim_filter = None
    if page_path:
        dim_filter = FilterExpression(filter=Filter(field_name="pagePath", 
            string_filter=Filter.StringFilter(match_type=Filter.StringFilter.MatchType.BEGINS_WITH, value=page_path)))

    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[Dimension(name="yearMonth")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date=f"{months*30}daysAgo", end_date="yesterday")],
        dimension_filter=dim_filter
    )
    
    response = client.run_report(request)

    # 3. 데이터 매칭
    for row in response.rows:
        raw_month = row.dimension_values[0].value # YYYYMM
        formatted_month = f"{raw_month[:4]}-{raw_month[4:]}"
        if formatted_month in results_dict:
            results_dict[formatted_month] = int(row.metric_values[0].value)

    # 4. 월순으로 정렬하여 반환
    return [{"month": k, "value": v} for k, v in sorted(results_dict.items())]

# 데이터 조립
stats = {
    "home": {
        "daily": get_daily_data(8),
        "monthly": get_monthly_data(4)
    },
    "about": {
        "daily": get_daily_data(8, page_path="/about"),
        "monthly": get_monthly_data(4, page_path="/about")
    }
}

os.makedirs('_data', exist_ok=True)
with open('_data/stats.json', 'w', encoding='utf-8') as f:
    json.dump(stats, f, indent=2, ensure_ascii=False)

print("Stats updated successfully!")