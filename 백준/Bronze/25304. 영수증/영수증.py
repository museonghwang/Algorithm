X = int(input())
N = int(input())

for i in range(N):
    a, b = list(map(int, input().split()))
    X -= a * b

print('Yes') if X == 0 else print('No')