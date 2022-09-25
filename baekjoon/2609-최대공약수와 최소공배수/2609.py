n, m = sorted(list(map(int, input().split())))

# 최대공약수: 두 수 이상의 여러 수의 공약수 중 최대인 수
for i in range(n, 0, -1):
    if n % i != 0:
        continue
    if m % i == 0:
        print(i)
        break

# 최소공배수: 두 수 이상의 여러 수의 공배수 중 최소인 수
i = 1
while True:
    if m * i % n == 0:
        print(m * i)
        break
    i += 1