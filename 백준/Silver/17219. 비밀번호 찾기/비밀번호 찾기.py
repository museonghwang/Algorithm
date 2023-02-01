import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a={}
for _ in range(n):
    a.setdefault(*input().rstrip().split())

for _ in range(m):
    sys.stdout.write(a[input().rstrip()]+'\n')