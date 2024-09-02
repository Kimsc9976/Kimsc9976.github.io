target = int(input())

n = 0
cnt = 0
while n < target:
    n += cnt
    cnt += 1
depth = cnt - 1
is_n_0 = True if depth % 2 else False
pref = sum([i for i in range(1,depth)])
to_walk = target - pref - 1 
div = f'{depth - to_walk}/{to_walk + 1}' if is_n_0 else f'{to_walk + 1}/{depth - to_walk}'
print(div)