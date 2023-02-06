import sys
input = sys.stdin.readline
n = int(input())
step = [int(input()) for i in range(n)]
DP = [0] * n

if n <= 2:
    print(sum(step))
else:
    DP[0] = step[0]
    DP[1] = step[0] + step[1]
    DP[2] = max(step[1] + step[2], step[0] + step[2])
    for i in range(3, n):
        DP[i] = max(
                step[i] + step[i-1] + DP[i-3],
                step[i] + DP[i-2]
            )
    print(DP[-1])