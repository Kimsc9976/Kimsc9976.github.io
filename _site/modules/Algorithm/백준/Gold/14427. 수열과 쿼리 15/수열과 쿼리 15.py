import sys
N = int(sys.stdin.readline())
As = [0]+ list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Qs = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]


segment_tree = [[0, 0] for _ in range(4*N+1)]


def tree(start, end, index):
    # start와 end가 같으면 리프노드
    if start == end :
        segment_tree[index] = [As[start], start]
    else:
        mid = (start+end) // 2
        left = index*2
        right = index*2+1
        tree(start, mid, left)   # 좌측으로
        tree(mid+1, end, right) # 우측으로
        
        small = left
        if segment_tree[left][0] > segment_tree[right][0]:
            small = right
        
        segment_tree[index] = [segment_tree[small][0], segment_tree[small][1]]


# 3. 트리 값 바꿔주기
def update(start, end, index, update_idx, update_data):
	# update 하려는 범위가 초과될 경우// (start,end) 범위에 없을 경우
    if start > update_idx or end < update_idx:
        return
    
    # 리프노드까지 바꿔주었으면 재귀함수를 끝낸다.
    if start == end:
        segment_tree[index] = [update_data, update_idx]
        return

	# update_idx가 관여하고 있는 노드들을 찾아서 바꿔준다.
    mid = (start + end) // 2
    left = index*2
    right = index*2+1
    # 다음 노드로 찾아간다.
    update(start, mid, index*2, update_idx, update_data)
    update(mid+1, end, index*2+1, update_idx, update_data)
    
    small = left
    if segment_tree[left][0] > segment_tree[right][0]:
        small = right
    
    segment_tree[index] = [segment_tree[small][0], segment_tree[small][1]]

tree(1, N, 1)
for Q in Qs:
    q, *items = Q

    if q == 1:
        update(1, N, 1, items[0], items[1])
    else:
        print(segment_tree[1][1])
