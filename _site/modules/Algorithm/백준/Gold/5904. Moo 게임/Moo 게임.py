N = int(input())

def daq(target, length ,cnt):
    if target <= 3:
        return 'm' if target == 1 else 'o'

    count = cnt + 3
    pre = length
    mid = pre + count
    next_length = length*2 + count
    
    pre_length = (length - (count-1))//2
    pre_mid = pre_length + (count-1)
    pre_end = pre_length*2 + (count-1)
    if target > next_length:
        return daq(target, next_length, cnt+1)
    
    elif target <= pre:
        target = target - pre if target - pre > 0 else target 
        return daq(target, pre_length, cnt-1)
    elif target <= mid:
        return 'm' if target == pre + 1 else 'o'
    elif target <= next_length:
        return daq(target-mid, pre_length, cnt-1)
ans = daq(N, 3, 1)
print(ans)