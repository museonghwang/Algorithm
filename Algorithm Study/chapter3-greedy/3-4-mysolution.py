n, k = map(int, input().split())

result = 0
while 1:
    if n == 1:
        break
    
    result += 1
    if n % k == 0:
        n /= k
    else:
        n -= 1

print(result)