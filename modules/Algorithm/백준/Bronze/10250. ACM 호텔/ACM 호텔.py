
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    H, W, M = map(int,sys.stdin.readline().split())

    Floor = M % H if (M%H != 0) else H
    room = M // H + 1 if (M%H != 0) else M // H
    print("{0}{1:0>2}".format(Floor, room))