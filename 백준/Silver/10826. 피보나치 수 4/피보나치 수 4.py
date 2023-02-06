import sys
DP = [-1]*10001
DP[0] = 0
DP[1] = 1

for i in range(2, 10001):
    DP[i] = DP[i-2] + DP[i-1]

print(DP[int(sys.stdin.readline())])