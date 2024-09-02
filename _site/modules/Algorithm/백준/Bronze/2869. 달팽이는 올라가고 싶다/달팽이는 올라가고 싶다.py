A, B, V = map(int,input().split())
day = (A-B)
for_up = (V-B)//day

if ((V-B)%day == 0):
    pass
else:
    for_up += 1

print(for_up)