import sys
n = int(sys.stdin.readline())
p = sorted(list(map(int, sys.stdin.readline().split())))
Pre=0
Sum=0
for i in range(n):
    Pre += p[i]
    Sum += Pre
print(Sum)