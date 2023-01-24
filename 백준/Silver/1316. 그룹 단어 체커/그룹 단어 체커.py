import sys

cnt = 0
for i in range(int(sys.stdin.readline())):
    word = sys.stdin.readline().rstrip()
    if list(word) == sorted(word, key=word.find):
        cnt += 1

print(cnt)