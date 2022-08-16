from sys import stdin

location = stdin.readline()
row = int(location[1])
col = int(ord(location[0])) - int(ord('a')) + 1

movable = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

count = 0
for move in movable:
    move_row = row + move[0]
    move_col = col + move[1]
    
    if move_row < 1 or move_col < 1 or move_row > 8 or move_col > 8:
        continue
    
    count += 1

print(count)