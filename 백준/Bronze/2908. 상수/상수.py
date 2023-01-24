import sys

a, b = sys.stdin.readline().rstrip().split()
print(max(int(a[::-1]), int(b[::-1])))