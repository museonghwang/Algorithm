import sys

S = sys.stdin.readline().rstrip()
print(*[S.find(chr(97+i)) for i in range(26)])