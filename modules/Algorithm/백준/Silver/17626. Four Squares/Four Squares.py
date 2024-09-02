def sol(num):
  if int(num**0.5) == num**0.5:
    return 1
  for i in range(1, int(num**0.5)+1):
    if int((num - i**2)**0.5) == (num - i**2)**0.5:
      return 2
  for i in range(1, int(num**0.5)+1):
    for j in range(1, int(num**0.5)+1):
      if((num - i**2 - j**2) < 0):
        break
      if int((num - i**2 - j**2)**0.5) == (num - i**2 - j**2)**0.5:
        return 3
  return 4
N = int(input())

print(sol(N))