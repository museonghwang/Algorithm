import sys
input()
a = list(map(int, sys.stdin.readline().split()))
a.sort()

for i in range(1, len(a)):
    a[i] += a[i-1]
print(sum(a))