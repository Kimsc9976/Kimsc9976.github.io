
def stars(Num):
  
  if Num == 3:
    return ['***', '* *', '***']
  
  a = [star*3 for star in stars(Num//3)] + [star + " "* (Num//3)+ star for star in stars(Num//3)] + [star*3 for star in stars(Num//3)]
  return a

result = stars(int(input()))
for i in range(len(result)):
  print(result[i])