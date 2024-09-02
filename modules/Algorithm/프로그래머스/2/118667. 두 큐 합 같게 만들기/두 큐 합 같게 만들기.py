from collections import deque


def solution(queue1, queue2):
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    if (sum1 + sum2) % 2 == 1: return -1
    if max(queue1) > (sum1+sum2) // 2 or max(queue2) > (sum1+sum2) // 2 : return -1

    
    max_count = (len(queue2) + len(queue1)) *2
    answer = 0
    while (sum1 != sum2) and (answer < max_count):
        if sum1 > sum2:
            x = queue1.popleft()
            queue2.append(x)
            sum2 += x
            sum1 -= x
        else:
            x = queue2.popleft()
            queue1.append(x)
            sum1 += x
            sum2 -= x

        answer += 1
        
    if answer >= max_count : 
        answer = -1
    
    return answer