import os
import json
import sys
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange, Dimension, Metric, RunReportRequest, OrderBy, FilterExpression, Filter
)

PROPERTY_ID = os.environ.get("GA_PROPERTY_ID")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

if not PROPERTY_ID:
    print("Error: GA_PROPERTY_ID is missing.")
    sys.exit(1)

client = BetaAnalyticsDataClient()

def get_daily_data(days, page_path=None):
    """최근 N일간의 데이터를 1일 단위로 추출 (선그래프용)"""
    dim_filter = None
    if page_path:
        dim_filter = FilterExpression(filter=Filter(field_name="pagePath", 
            string_filter=Filter.StringFilter(match_type=Filter.StringFilter.MatchType.BEGINS_WITH, value=page_path)))

    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[Dimension(name="date")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date=f"{days}daysAgo", end_date="yesterday")],
        dimension_filter=dim_filter,
        order_bys=[OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name="date"))]
    )
    response = client.run_report(request)
    return [{"date": f"{row.dimension_values[0].value[:4]}-{row.dimension_values[0].value[4:6]}-{row.dimension_values[0].value[6:]}", 
             "value": int(row.metric_values[0].value)} for row in response.rows]

def get_monthly_data(months, page_path=None):
    """최근 N개월간의 데이터를 1달 단위로 추출 (막대그래프용)"""
    dim_filter = None
    if page_path:
        dim_filter = FilterExpression(filter=Filter(field_name="pagePath", 
            string_filter=Filter.StringFilter(match_type=Filter.StringFilter.MatchType.BEGINS_WITH, value=page_path)))

    request = RunReportRequest(
        property=f"properties/{PROPERTY_ID}",
        dimensions=[Dimension(name="yearMonth")],
        metrics=[Metric(name="activeUsers")],
        date_ranges=[DateRange(start_date=f"{months*30}daysAgo", end_date="yesterday")],
        dimension_filter=dim_filter,
        order_bys=[OrderBy(dimension=OrderBy.DimensionOrderBy(dimension_name="yearMonth"))]
    )
    response = client.run_report(request)
    return [{"month": f"{row.dimension_values[0].value[:4]}-{row.dimension_values[0].value[4:]}", 
             "value": int(row.metric_values[0].value)} for row in response.rows]

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