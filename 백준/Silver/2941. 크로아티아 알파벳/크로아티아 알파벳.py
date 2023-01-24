import sys

a = sys.stdin.readline().rstrip()
for i in ['c=','c-','dz=','d-','lj','nj','s=','z=']:
    if i in a:
        a = a.replace(i, ' ')
    else: continue

print(len(a))