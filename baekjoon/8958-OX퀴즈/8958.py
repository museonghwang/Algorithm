n = int(input())

for _ in range(n):
    result = 0
    dummy = 0
    for i in input():
        if i == 'O':
            dummy += 1
            result += dummy
        else:
            dummy = 0
    
    print(result)