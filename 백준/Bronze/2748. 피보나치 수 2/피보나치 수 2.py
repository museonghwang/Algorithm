import sys
DP = {0:0, 1:1}

def fibo(n):
    if n in DP: return DP[n]
    else:
        DP[n] = fibo(n-1) + fibo(n-2)
        return DP[n]

print(fibo(int(sys.stdin.readline())))