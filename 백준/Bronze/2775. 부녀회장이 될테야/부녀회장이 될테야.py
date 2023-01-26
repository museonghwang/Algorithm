from math import factorial
import sys

for i in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(int(factorial(k+n)/(factorial(n-1)*factorial(k+1))))