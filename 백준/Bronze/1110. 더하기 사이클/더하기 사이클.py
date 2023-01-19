N = int(input())
END = N
count = 0

while True:
    N = N%10*10 + (N//10 + N%10) % 10
    count += 1
    if END == N: break

print(count)