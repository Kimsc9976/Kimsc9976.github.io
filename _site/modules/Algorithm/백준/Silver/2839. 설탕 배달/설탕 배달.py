import sys
N = int(sys.stdin.readline())

def dev(num):
    rlt = 0
    if num%5 ==0:
        rlt = num//5
        return rlt
    else:
        Num_cpy = num
        while Num_cpy >0:
            Num_cpy -= 3
            rlt += 1
            if Num_cpy % 5 == 0:
                rlt += Num_cpy//5
                return rlt
        rlt = num//3 if num%3 == 0 else -1
        return rlt
print(dev(N))