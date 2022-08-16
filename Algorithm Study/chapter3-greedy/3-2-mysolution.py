_, M, K = map(int, input().split())
input_data = list(map(int, input().split()))

input_data.sort(reverse=True)
first_data = input_data[0] # 첫번째로 큰 수
second_data = input_data[1] # 두번째로 큰 수

result = 0

for m in range(M):
    if m == 0:
        result += first_data
        continue
    
    if m % K == 0:
        result += second_data
    else:
        result += first_data

print(result)