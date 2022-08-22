from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())

maze_map = []
for _ in range(n):
    maze_map.append(list(map(int, stdin.readline().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maze_map[nx][ny] == 0:
                    continue
                if maze_map[nx][ny] == 1:
                    maze_map[nx][ny] = maze_map[x][y] + 1
                    queue.append((nx, ny))
    return maze_map[n-1][m-1]

print(bfs(0, 0))