import sys
from math import factorial

fac = str(factorial(int(sys.stdin.readline())))
cnt = 0

for i in fac[::-1]:
    if i != '0':
        break
    cnt += 1

print(cnt)