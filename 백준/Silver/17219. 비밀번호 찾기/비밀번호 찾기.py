import sys
input=sys.stdin.readline
n,m=map(int,input().split())

a=dict(input().split() for _ in range(n))
print("\n".join([a[input().strip()] for _ in range(m)]))