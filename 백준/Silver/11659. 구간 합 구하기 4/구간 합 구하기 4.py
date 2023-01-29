import sys
input = sys.stdin.readline
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp + i
    prefix_sum.append(temp) # 합 배열 만들기

for _ in range(M):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start-1]) # 합 배열에서 구간 합 구하기