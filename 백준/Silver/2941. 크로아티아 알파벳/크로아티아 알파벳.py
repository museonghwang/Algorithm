import sys

ALPHA = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = sys.stdin.readline().rstrip()

for i in ALPHA:
    check = True
    while check:
        if i in a:
            a = a.replace(i, ' ', 1)
        else:
            check = False

print(len(a))