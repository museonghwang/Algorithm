import sys

for _ in range(int(sys.stdin.readline())):
    R, S = sys.stdin.readline().rstrip().split()    
    print(*[i*int(R) for i in S], sep='')