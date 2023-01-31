import sys
n, k = map(int, sys.stdin.readline().split())
a = sorted([int(sys.stdin.readline()) for _ in range(n)], reverse=True)

cnt = 0
for i in a:
    if k < i: continue
    if k < 0:
        print(cnt)
        break
    cnt += k // i
    k = k % i
print(cnt)