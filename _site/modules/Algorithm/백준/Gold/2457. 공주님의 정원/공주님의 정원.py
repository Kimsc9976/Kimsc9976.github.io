import sys

# 꽃들의 총 개수 N
n = int(sys.stdin.readline())

# 꽃들이 피고 지는 날짜
arr = []
for _ in range(n):
    # 꽃이 피고 지는 날짜에 대해 월에 100을 곱한 뒤, 일이랑 덧셈
    start_m, start_d, end_m, end_d = map(int, sys.stdin.readline().split())
    arr.append([start_m * 100 + start_d, end_m * 100 + end_d])

# 꽃이 피는 날짜, 꽃이 지는 날짜순으로 오름차순 정렬
arr.sort()

# 정원의 마지막 꽃이 지는 날짜 <- 시작일 301
end_date = 301

# 심은 꽃의 개수
count = 0

# 더 이상 확인할 꽃이 없을때까지
while (arr):

    # 정원의 마지막 꽃이 지는 날짜가 12월 1일 이상이 됐거나,
    # 현재 확인할 꽃의 시작 날짜가 정원의 마지막 꽃이 지는 날짜와 이어지지 않을 경우, 탐색 종료
    if (end_date >= 1201 or arr[0][0] > end_date):
        break

    # 꽃이 피는 날짜가 end_date 이전일 때, 가장 느리게 지는 꽃의 날짜
    temp_end_date = -1

    for _ in range(len(arr)):

        # 꽃이 피는 날짜가 end_date 이전이라면,
        if (arr[0][0] <= end_date):
            # 그 중 가장 느리게 지는 꽃의 날짜를 확인
            if (temp_end_date <= arr[0][1]):
                temp_end_date = arr[0][1]

            # 확인한 꽃은 원본 배열에서 제거
            arr.remove(arr[0])

        else:
            break

    # 가장 꽃이 느리게 지는 날짜를 end_date로 수정
    end_date = temp_end_date
    # 심은 꽃의 개수 증가
    count += 1

# 마지막으로 확인한 꽃의 지는 날짜가 12월 1일 보다 작으면, 
# 3월 1일부터 11월 30일까지 계속 피어있는게 아니므로 0 출력
if end_date < 1201:
    print(0)
else:
    print(count)
