from sys import stdin

while True:
    dummy = list(map(int, stdin.readline().split()))
    dummy.sort()
    
    if sum(dummy) == 0:
        break
    elif dummy[2]**2 == dummy[0]**2 + dummy[1]**2:
        print('right')
    else:
        print('wrong')