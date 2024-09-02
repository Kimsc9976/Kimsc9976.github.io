def solution(name, yearning, photo):
    N = len(name)
    answer = [0 for _ in range(len(photo))]
    points = {name[i] : yearning[i] for i in range(N)}
    
    for idx, img in enumerate(photo):
        count = 0
        for person in img:
            if points.get(person) : count += points[person] 
        answer[idx] = count
    
    return answer