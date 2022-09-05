n = int(input())
str = input()

H = 0
for i in range(n):
    H += (ord(str[i])-96) * 31 ** i

print(H % 1234567891)