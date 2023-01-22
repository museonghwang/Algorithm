import sys

N = int(sys.stdin.readline())

if N <= 99:
    print(N)
else:
    cnt = 0
    for i in range(100, N+1):
        i = list(map(int, str(i)))
        if i[0]-i[1] == i[1]-i[2]:
            cnt += 1
    print(99 + cnt)
