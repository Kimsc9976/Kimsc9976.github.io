
A, B, C = map(int,input().split())


def son_ik(a,b,c):
    if B>= C:
        return -1
    x = a//(c-b) + 1
    return x

print(son_ik(A,B,C))
