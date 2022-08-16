N, _ = map(int, input().split())

result = 0
for i in range(N):
    dummy = min(list(map(int, input().split())))
    result = max(dummy, result)

print(result)