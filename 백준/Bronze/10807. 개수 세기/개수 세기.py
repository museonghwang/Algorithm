N = int(input())
dummy = list(map(int, input().split()))
v = int(input())
cnt = 0

for i in dummy:
    if v == i: cnt += 1

print(cnt)