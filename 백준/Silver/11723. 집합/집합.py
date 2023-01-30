import sys
input = sys.stdin.readline
S = set()
for _ in range(int(input())):
    pack = input().rstrip().split()
    if pack[0]=='add': S.add(int(pack[1]))
    elif pack[0]=='remove': S.discard(int(pack[1]))
    elif pack[0]=='check': print(1 if int(pack[1]) in S else 0)
    elif pack[0]=='toggle':
        S.discard(int(pack[1])) if int(pack[1]) in S else S.add(int(pack[1]))
    elif pack[0]=='all': S = set(range(1, 21));
    elif pack[0]=='empty': S.clear()