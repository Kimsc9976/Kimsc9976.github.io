from itertools import permutations
N = int(input())
games=[list(map(int,input().split())) for _ in range(N)]

max_score = 0

for items in permutations(range(2,10), 8):
  score = 0
  player = items[:3] + (1,) + items[3:]
  inning = 0
  idx = 0
  while inning < N:
    game = games[inning]
    out_count = 0
    player_idx = idx
    base = [0,0,0,0]
    while out_count < 3:
      py = player[player_idx] - 1 # 선수 등번호
      g = game[py] # 몇루타 인지 확인하는
      if g == 0: out_count += 1
      else:
        for plate in (3,2,1):
          if base[plate] == 1:
            mv = plate + g # 루타 만큼 이동
            if mv >= 4:
              base[0] += 1
              base[plate] = 0
            else:
              base[mv] = 1
              base[plate] = 0
        base[g%4] += 1
      player_idx = (player_idx + 1)%9
    idx = player_idx
    score += base[0]
    inning += 1
  max_score = max_score if max_score > score else score
print(max_score)
  