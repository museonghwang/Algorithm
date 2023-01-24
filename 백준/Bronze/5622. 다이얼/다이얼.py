import sys

DIAL = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0

for i in sys.stdin.readline().rstrip():
    for j in DIAL:
        if i in j:
            time += DIAL.index(j)+3

print(time)