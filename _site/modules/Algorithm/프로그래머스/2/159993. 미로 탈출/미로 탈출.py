from collections import deque

def getItems(_map):
    start = [0, 0]
    laver = [0, 0]
    end = [0, 0]
    
    x = 0
    count = 0
    for item in _map:
        y = 0
        for c in item:
            if c == "E" : 
                count += 1
                end = [x, y]
            if c == "S" :
                count += 1
                start = [x, y]
            if c == "L" :
                count += 1
                laver = [x, y]
            y += 1
        
        x += 1
        if count == 3 : 
            return {
                "start" : start,
                "laver" : laver,
                "end" : end
            }
    return {
        "start" : start,
        "laver" : laver,
        "end" : end
    } 
    
    
def bfs(start_point, end_point, maps):
    N = len(maps)
    M = len(maps[0])
    
    is_visited = [[ False for _ in range(M) ] for _ in range(N) ]
    
    que = deque()
    que.append([start_point, 0])
    is_visited[start_point[0]][start_point[1]] = True
    
    while que:
        now, depth = que.popleft()
        
        if now == end_point: return depth
        
        x, y = now
        
        for dx, dy in [(0,1), (0, -1), (1,0), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M : continue
            if maps[nx][ny] == "X" : continue
            if is_visited[nx][ny] : continue
            
            is_visited[nx][ny] = True
            que.append([[nx, ny], depth+1])
        
    
def solution(maps):
    answer = 0
        


    points = getItems(maps)
    
    
    to_laver = bfs(points["start"], points["laver"], maps)
    to_end = bfs(points["laver"], points["end"], maps)
    
    if to_laver and to_end : answer = to_laver + to_end
    else : answer = -1
    
    return answer