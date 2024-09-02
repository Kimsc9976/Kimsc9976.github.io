def solution(park, routes):
    
    d = {
        "N" : [-1, 0],
        "S" : [1, 0],
        "W" : [0, -1],
        "E" : [0, 1],
    }
    
    
    X = len(park)
    Y = len(park[0])
    
    flag = False
    x = 0
    for par in park:
        y = 0
        for c in par:
            if c == "S":
                flag = True
                break
            y += 1
        if flag:
            break
        x += 1
    
    answer = [x, y]
    
    for route in routes:
        direction = d[route[0]]
        move = route[2]

    
        for n in range(1, int(move)+1):
            nx = answer[0] + direction[0] * n
            ny = answer[1] + direction[1] * n
            
            if nx < 0 or ny < 0 or nx >= X or ny >= Y : break
            if park[nx][ny] == "X" : break
        else:
            answer = [nx, ny]   
    
    return answer