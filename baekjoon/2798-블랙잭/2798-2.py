from itertools import combinations
from sys import stdin

_, m = map(int, stdin.readline().split())
case = list(map(int, stdin.readline().split()))
result = 0

for c in combinations(case, 3):
    if sum(c) > m:
        continue
    else:
        result = max(result, sum(c))

print(result)