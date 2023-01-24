import sys

DIAL = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0

for i in sys.stdin.readline().rstrip():
    for j in range(len(DIAL)):
        if i in DIAL[j]:
            time += (j+3)

print(time)