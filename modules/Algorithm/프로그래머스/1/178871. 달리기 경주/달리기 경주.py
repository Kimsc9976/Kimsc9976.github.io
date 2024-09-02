def solution(players, callings):
    answer = []
    ranking = { _key : idx for idx, _key in enumerate(players) }
    
    for call in callings:
        rank = ranking[call]
        
        p1 = players[rank]
        p2 = players[rank-1]
    
        ranking[p1] = rank - 1
        ranking[p2] = rank
    
        players[rank], players[rank - 1] = players[rank - 1], players[rank]
    
    
    return players