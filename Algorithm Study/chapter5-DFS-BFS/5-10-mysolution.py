from sys import stdin

n, m = map(int, stdin.readline().split())

ice_map = []
for _ in range(n):
    ice_map.append(list(map(int, stdin.readline().strip())))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    else:
        if ice_map[x][y] == 0:
            ice_map[x][y] = 1
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            return True
        else:
            return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1

print(count)