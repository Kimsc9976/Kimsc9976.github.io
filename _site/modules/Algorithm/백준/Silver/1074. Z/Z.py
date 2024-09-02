Z, r, c = map(int,input().split())

N = 2**Z

def rangemaker(row, col, size):
    
    rng_x = [row, row+size]
    rng_y = [col, col+size]
    
    return [rng_x, rng_y]

def check(target, *args):
    x,y = target[0],target[1]
    place = 0
    for arg in args:
        row, col = rangemaker(arg[0],arg[1],arg[2])
        
        if x in range(*row) and y in range(*col):
            return arg, place
        place += 1
        
    return None

numb = 0
def sol(target, row, col, size, depth):
    global numb
    if target == (row, col):
        return 
    new_size = size//2
    node1 = (row, col, new_size)
    node2 = (row, col + new_size, new_size)
    node3 = (row + new_size, col, new_size)
    node4 = (row + new_size, col + new_size, new_size)
    
    next, node = check(target, node1, node2, node3, node4)
    
    if next[2] != 1 : # size 가 1이 아닐 경우
        numb += size**2 * node// 4 
    else : 
        numb += node
    sol(target, *next, depth+1)

sol((r,c), 0, 0, N, 0)
print(numb)
