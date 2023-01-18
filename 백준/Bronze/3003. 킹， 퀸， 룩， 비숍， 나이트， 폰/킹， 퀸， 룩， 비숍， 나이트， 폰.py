chess = [1, 1, 2, 2, 2, 8]
chess_set = list(map(int, input().split()))

for i in range(len(chess)):
    print(chess[i] - chess_set[i], end=' ')