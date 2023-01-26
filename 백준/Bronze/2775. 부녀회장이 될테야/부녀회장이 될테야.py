# k층 n호 = (k+n)! / ((n-1)! * (k+1)!)
# 1층 3호 = 6  = 4C2 = 4! / 2!2!
# 2층 3호 = 10 = 5C3 = 5! / 2!3!

from math import factorial

for i in range(int(input())):
    k = int(input())
    n = int(input())
    print(int(factorial(k+n)/(factorial(n-1)*factorial(k+1))))