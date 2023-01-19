A, B = map(int, input().split())
C = int(input())

A += C // 60
B += C % 60

if B >= 60:
    A += B // 60
    B = B % 60

if A >= 24:
    A -= 24

print(A, B)