import sys

a = [i for i in range(1, 31)]
b = [int(sys.stdin.readline()) for i in range(28)]

for i in range(30):
    if a[i] not in b: print(a[i])