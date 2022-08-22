from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    h, _, n = map(int, stdin.readline().split())
    
    floor = n % h
    line = n // h + 1
    if floor == 0:
        floor = h
        line -= 1       
    print(floor * 100 + line)