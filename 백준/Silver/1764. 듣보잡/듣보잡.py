import sys 
input = sys.stdin.readline
n, m = map(int, input().split())

not_listen = {input() for _ in range(n)}
ans = []
for i in range(m):
    not_seen = input()
    if not_seen in not_listen:
        ans.append(not_seen)

print(len(ans))
print(''.join(sorted(ans)))