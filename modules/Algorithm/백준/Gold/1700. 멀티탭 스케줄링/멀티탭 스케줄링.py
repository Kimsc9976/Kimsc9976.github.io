
import sys
N, K = map(int, sys.stdin.readline().split())
items = list(map(int, sys.stdin.readline().split()))

# 멀티탭에 현재 꽂혀 있는 기기
plugs = set()
# 교체 횟수
changes = 0

for i in range(K):
    # 현재 기기가 이미 멀티탭에 꽂혀있다면, 건너뛰기
    if items[i] in plugs:
        continue

    # 멀티탭에 빈 자리가 있다면, 바로 꽂기
    if len(plugs) < N:
        plugs.add(items[i])
        continue

    # 멀티탭이 가득 차면 교체할 기기 선택
    # 멀티탭에 꽂힌 기기 중 다음 사용까지의 시간이 가장 긴 기기를 찾기
    indices = {item: float('inf') for item in plugs}
    for j in range(i+1, K):
        if items[j] in indices and indices[items[j]] == float('inf'):
            indices[items[j]] = j
    
    # 가장 나중에 사용될 기기 혹은 더 이상 사용되지 않을 기기를 찾아 제거
    to_remove = max(indices, key=indices.get)
    plugs.remove(to_remove)
    plugs.add(items[i])
    changes += 1

print(changes)