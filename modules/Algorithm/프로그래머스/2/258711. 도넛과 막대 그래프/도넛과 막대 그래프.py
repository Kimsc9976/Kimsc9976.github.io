def solution(edges):
    max_num = 0
    for edge in edges:
        max_num = max(max_num, max(edge))
        
        
    nodes = dict()
    for a, b in edges:
        
        if not nodes.get(a):
            nodes[a] = [0, 0]
        if not nodes.get(b):
            nodes[b] = [0, 0]
            
        # 0은 주는거 1은 받는거
        nodes[a][0] += 1 
        nodes[b][1] += 1
    
    # 받는거 1개도 없으면 생성자 
    ## 막대기와 중복이 생길 수 있는데, 막대기와 다른점은 주는게 1개 더있음 
    ## 따라서 주는거 2개로 작업
    
    # 주는거 1개 받는거 1개 = 도넛
    # 주는거 1개 받는거 0개 = 막대
    # 주는거 1개 받는거 1개or 2개 = 8자
    
    head = 0
    donuts = 0
    stick = 0
    eight = 0
    for key, links in nodes.items():
        
        # 생성자 : 
        if links[0] >= 2 and links[1] == 0:
            head = key
            
        # # 도넛 : 두개받고 하나 주는게 있음
        # if links[0] == 1 and  links[1] == 2:
        #     donuts += 1
        
        # 막대기 : 끝에가면 받는거만 있지 주는게 없음
        if links[0] == 0 and  links[1] > 0:
            stick += 1
        
        # 8자 : 중간에 2개씩 주고받는게 있음
        if links[0] >= 2 and  links[1] >= 2:
            eight += 1
        
    answer = [0]
    donuts = nodes[head][0] - stick - eight

    return [head, donuts, stick, eight]