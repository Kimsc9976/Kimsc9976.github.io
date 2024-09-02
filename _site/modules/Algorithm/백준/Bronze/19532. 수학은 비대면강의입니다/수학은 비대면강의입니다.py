a1, b1, c1, a2, b2, c2 = map(int,input().split())
x = (c1*b2 - c2*b1)//(b2*a1 - b1*a2)
y = (c1*a2 - c2*a1)//(b1*a2 - b2*a1)
print(x, y)