from sys import stdin

n, m = map(int, stdin.readline().split())
x, y, d = map(int, stdin.readline().split())

map_init = [list(map(int, stdin.readline().split())) for _ in range(n)] # 초기화 지도 생성
visited = [[False] * m for _ in range(n)] # 방문한 곳 인식
visited[x][y] = True # 초기 위치는 1로 처리

movable_check = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북, 동, 남, 서
move_count = 1 # 이동 횟수
turn_count = 0 # 회전 횟수

while True:
    # 왼쪽으로 회전
    d = 3 if d == 0 else d - 1

    mx = x + movable_check[d][0]
    my = y + movable_check[d][1]
    
    # 왼쪽회전 후 가보지도 않았고, 육지인 칸이 존재한다면
    if visited[mx][my] == False and map_init[mx][my] == 0:
        x, y = mx, my
        visited[mx][my] = True
        move_count += 1 # 이동 횟수
        turn_count = 0 # 회전 횟수
    else:
        turn_count += 1
    
    # 4개 방향으로 모두 갈 수 없다면 뒤로 이동(단, 바다면 안됨)
    if turn_count == 4:
        mx = x - movable_check[d][0]
        my = y - movable_check[d][1]
        
        if map_init[mx][my] == 0:
            x, y = mx, my
        else:
            break
        turn_count = 0
    
print(move_count)