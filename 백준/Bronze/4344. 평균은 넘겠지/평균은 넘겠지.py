import sys

for i in range(int(sys.stdin.readline())):
    a = list(map(int, sys.stdin.readline().split()))
    count = 0
    for j in a[1:]:
        if j > sum(a[1:])/a[0]: count += 1
    
    print('{:0.3f}%'.format(count/a[0]*100))