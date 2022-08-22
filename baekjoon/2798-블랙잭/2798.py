from sys import stdin

n, m = map(int, stdin.readline().split())
case = list(map(int, stdin.readline().split()))

result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if case[i] + case[j]+ case[k] > m:
                continue
            else:
                result = max(result, case[i] + case[j]+ case[k])

print(result)