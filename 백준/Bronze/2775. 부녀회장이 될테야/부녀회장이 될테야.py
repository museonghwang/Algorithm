from math import factorial as f
import sys

input = sys.stdin.readline
for i in range(int(input())):
    k = int(input()); n = int(input())
    print(int(f(k+n)/(f(n-1)*f(k+1))))