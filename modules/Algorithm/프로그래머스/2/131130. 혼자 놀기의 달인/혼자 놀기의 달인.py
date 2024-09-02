def solution(cards):
    length = len(cards)
    is_visited = [False for _ in range(length)]
    box = list()
    
    for i in range(length) :
        if not is_visited[i] :
            idx = i
            cnt = 0
            while not is_visited[idx] :
                cnt += 1
                is_visited[idx] = True
                idx = cards[idx] - 1
            box.append(cnt)
    box.sort(reverse = True)
    box.append(0)
    
    return box[0]*box[1]
