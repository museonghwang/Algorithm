import sys
input = sys.stdin.readline
s = [int(input()) for _ in range(int(input()))]

m = max(s)
cnt = 1
chk = s.pop()
if m == chk:
    print(cnt)
else:
    while True:
        now = s.pop()
        if now > chk:
            cnt += 1
            chk = now
        if m == now:
            print(cnt)
            break