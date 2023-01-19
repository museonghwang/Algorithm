n = int(input())
test_score = list(map(int, input().split()))
max_score = max(test_score)

for i in range(n):
    test_score[i] = test_score[i] / max_score * 100

result = sum(test_score) / n
print(result)