import sys

for _ in range(int(sys.stdin.readline())):
    sum = 0; count = 0
    for i in sys.stdin.readline():
        if i == 'O':
            count += 1; sum += count
        else: count = 0
    print(sum)