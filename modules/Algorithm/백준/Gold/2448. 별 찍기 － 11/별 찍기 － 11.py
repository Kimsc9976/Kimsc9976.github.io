def stars(num):
    if num == 3:
        return ['  *  ', ' * * ','*****']
    s = [' '*(num//2) +star+' '*(num//2) for star in stars(num//2)]+[star + ' '+ star for star in stars(num//2)]
    return s

result = stars(int(input()))
for _ in result:
    print(_)