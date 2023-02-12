import sys
a = sys.stdin.readline().rstrip()

for _ in range(50):
    a=a.replace('()', '')

print(len(a))