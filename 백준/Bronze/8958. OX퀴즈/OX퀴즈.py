import sys

for i in range(int(sys.stdin.readline())):
    sum = 0; count = 0
    a = sys.stdin.readline()
    for j in a:
        if j == 'O':
            count += 1; sum += count
        else: count = 0
    print(sum)