from sys import stdin, stdout
input = stdin.readline
print = stdout.write
n, m = map(int, input().split())
a = {input().rstrip():i for i in range(1, n+1)}
convert_a = {v:k for k,v in a.items()}

for i in range(m):
    cmd = input().rstrip()
    print(str(a[cmd])+'\n') if cmd in a else print(convert_a[int(cmd)]+'\n')