while True:
    n = input()
    if n == '0':
        break
    
    check = 'yes'
    for i in range(len(n)//2):
        if n[i] != n[len(n)-i-1]:
            check = 'no'
            break
    
    print(check)