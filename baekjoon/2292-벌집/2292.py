'''
숫자범위      마지막 수 수식       정답    계수 차이
1           1 + (6 * 0)       1        0
2 ~ 7       1 + (6 * 1)       2        1
8 ~ 19      1 + (6 * 2)       3        2
20 ~ 37     1 + (6 * 3)       4        3
'''

from sys import stdin

n = int(stdin.readline())
count = 1

while n > 1:
    n -= count * 6
    count += 1

print(count)