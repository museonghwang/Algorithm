import sys
for i in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().split()
    a.reverse()
    print(f'Case #{i+1}:', *a)