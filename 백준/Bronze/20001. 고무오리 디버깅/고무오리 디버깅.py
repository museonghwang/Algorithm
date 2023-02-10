import sys
sys.stdin.readline().rstrip()

num = 0
while 1:
    debug = sys.stdin.readline().rstrip()
    if debug == '문제': num += 1
    elif debug == '고무오리':
        if num > 0: num -= 1
        else: num += 2
    else: 
        if num > 0: print('힝구')
        else: print('고무오리야 사랑해')
        break