from math import factorial
import sys

input = sys.stdin.readline
for i in range(int(input())):
    k = int(input())
    n = int(input())
    print(int(factorial(k+n)/(factorial(n-1)*factorial(k+1))))