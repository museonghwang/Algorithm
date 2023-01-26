import math

T = int(input())

for i in range(T):
    k = int(input())
    n = int(input())
    
    print(int(math.factorial(k+n)/(math.factorial(n-1)*math.factorial(k+1))))