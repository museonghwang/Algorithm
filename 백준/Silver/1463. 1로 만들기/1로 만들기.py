import sys
n = int(sys.stdin.readline())
dp = {1: 0, 2:1, 3:1}

def f(n):
    if n in dp: return dp[n]
    if n % 3 == 0 and n % 2 == 0:
        dp[n] = 1 + min(f(n//3), f(n//2))
        return dp[n]
    if n % 3 == 0 and n % 2 != 0:
        dp[n] = 1 + min(f(n-1), f(n//3))
        return dp[n]
    if n % 3 != 0 and n % 2 == 0:
        dp[n] = 1 + min(f(n-1), f(n//2))
        return dp[n]
    else:
        dp[n] = 1 + f(n-1)
        return dp[n]

print(f(n))