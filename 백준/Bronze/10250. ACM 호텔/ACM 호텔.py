import sys, math
for i in range(int(input())):
    H, W, N = map(int, sys.stdin.readline().split())
    line = math.ceil(N/H)
    # 층수
    while N > H:
        
        N -= H
        
    print(N*100 + line) # 호수