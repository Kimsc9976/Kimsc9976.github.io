R,C,T = map(int,input().split())

rooms = [list(map(int,input().split())) for _ in range(R)]
dx = (-1,0,1,0)
dy = (0,1,0,-1)

def flying_munzi(x,y, _munzi : dict):
    mz = rooms[x][y]
    if not _munzi.get((x,y)):
        _munzi[(x,y)] = 0
    diffuse = mz//5
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx<0 or ny<0 or nx>=R or ny>=C:
            continue
        if rooms[nx][ny] == -1:
            continue

        if not _munzi.get((nx,ny)):
            _munzi[(nx,ny)] = 0

        _munzi[(nx,ny)] += diffuse
        mz -= diffuse
    _munzi[(x,y)] += mz
    return _munzi

def clean_munzi(clnr):

    top_x, top_y = clnr[0]
    bot_x, bot_y = clnr[1]

    top_moving = 0
    top_x = top_x + dx[top_moving]
    top_y = top_y + dy[top_moving]
    next_tx = top_x
    next_ty = top_y

    while rooms[top_x][top_y] != -1:
        
        if next_tx <= 0 or next_tx >= clnr[0][0] or next_ty <= 0 or next_ty >= C - 1:
            if (next_tx == 0 and next_ty == 0) or (next_tx == 0 and next_ty == C - 1) or (next_tx == clnr[0][0] and next_ty == C - 1):
                top_moving = (top_moving +1)%4

        next_tx = top_x + dx[top_moving]
        next_ty = top_y + dy[top_moving]

        if rooms[next_tx][next_ty] != -1:
            rooms[top_x][top_y] = rooms[next_tx][next_ty]
            rooms[next_tx][next_ty] = 0

        top_x = next_tx
        top_y = next_ty



    bot_moving = 2
    bot_x = bot_x + dx[bot_moving]
    bot_y = bot_y + dy[bot_moving]

    next_bx = bot_x
    next_by = bot_y
    while rooms[bot_x][bot_y] != -1:
        if next_bx <= clnr[1][0] or next_bx >= R-1 or next_by <= 0 or next_by >= C - 1:
            if (next_bx == R-1 and next_by == 0) or (next_bx == R-1 and next_by == C - 1) or (next_bx == clnr[1][0] and next_by == C - 1):
                bot_moving = (bot_moving -1)%4

        next_bx = bot_x + dx[bot_moving]
        next_by = bot_y + dy[bot_moving]

        if rooms[next_bx][next_by] != -1:
            rooms[bot_x][bot_y] = rooms[next_bx][next_by]
            rooms[next_bx][next_by] = 0

        bot_x = next_bx
        bot_y = next_by
    

def time_out():
    time = 0

    while time <T:
        time += 1

        munzi = dict()
        cleaner =[]
        for i in range(R):
            for j in range(C):
                if rooms[i][j] == -1 :
                    cleaner.append((i,j))
                elif rooms[i][j] != 0:
                    munzi = flying_munzi(i,j, munzi)
                    rooms[i][j] = 0
        
        for a,b in munzi:
            rooms[a][b] = munzi[(a,b)]

        clean_munzi(cleaner)

    rlt = 0
    for i in range(R):
        for j in range(C):
            if rooms[i][j] != -1 and rooms[i][j] != 0:
                rlt += rooms[i][j]

    return rlt

print(time_out())