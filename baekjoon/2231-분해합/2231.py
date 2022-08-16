from sys import stdin

n = int(stdin.readline())

result = 0
for i in range(1, n+1):
    s = i + sum(list(map(int, str(i))))
    if(s == n):
        result = i
        break

print(result)