def solution(picks, minerals):
    
    def dfs(is_used, miner_, piro, end, picks, minerals):
        nonlocal answer
        
        if miner_ >= end:
            answer = min(piro, answer)
            return

        if is_used == picks:
            answer = min(piro, answer)
            return

        if piro >= answer:
            return

        if is_used[0] < picks[0]: # 다이아
            is_used[0] += 1
            dfs(is_used, miner_+5, piro + check(0,miner_, minerals), end, picks, minerals)
            is_used[0] -= 1

        if is_used[1] < picks[1]: # 철
            is_used[1] += 1
            dfs(is_used, miner_+5, piro + check(1,miner_, minerals), end, picks, minerals)
            is_used[1] -= 1

        if is_used[2] < picks[2]: # 돌
            is_used[2] += 1
            dfs(is_used, miner_+5, piro + check(2,miner_, minerals), end, picks, minerals)
            is_used[2] -= 1
    
    end = len(minerals)
    answer = 25*end + 1
    is_used = [0,0,0]
    
    addi = 5 - end % 5
    
    for _ in range(addi):
        minerals += ["none"]
    
    dfs(is_used,0,0,end, picks, minerals)

    return answer

def check(pick, now_m, minerals):
    rlt = 0
    matrix = [[1,1,1],[5,1,1],[25,5,1]]
    mines = {"diamond":0, "iron":1, "stone":2, "none":3}
    for i in range(5):
        mine = now_m + i
        mine = minerals[mine]
        mine = mines[mine]
        if mine == 3: continue
        rlt += matrix[pick][mine]
    return rlt
        
        

        