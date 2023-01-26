import sys
for _ in range(int(input())):
    H, _, N = map(int, sys.stdin.readline().split())
    floor = N%H; line = N//H+1
    if floor == 0: floor = H; line -= 1
    print(floor*100 + line)