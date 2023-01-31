import sys
input = sys.stdin.readline
n, m = map(int, input().split())

a = {input().rstrip() for _ in range(n)}
b = {input().rstrip() for _ in range(m)}

print(len(a & b))
print(*sorted(a & b), sep='\n')