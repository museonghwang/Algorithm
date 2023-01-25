import sys
A, B, C = map(int, sys.stdin.readline().split())
print(-1) if B>=C else print(int(A/(C-B))+1)