import sys
n = int(sys.stdin.readline())
p = sorted(list(map(int, sys.stdin.readline().split())))

prefix_sum = []
m = 0
for i in p:
    m += i
    prefix_sum.append(m)

print(sum(prefix_sum))