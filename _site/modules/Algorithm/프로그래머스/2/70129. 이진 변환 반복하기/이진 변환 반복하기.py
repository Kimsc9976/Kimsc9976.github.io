def solution(s):

    count_iter = 0
    count_0 = 0
    
    while s != '1':
        num_1 = 0
        for c in s:
            if c == '1' : num_1 += 1
            else: count_0 += 1

        s = format(num_1, 'b')
        count_iter += 1
    
    return [count_iter, count_0]