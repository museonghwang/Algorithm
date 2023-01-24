a = set(range(1, 10000))
nonSelfNum = set()

for i in range(1, 10001):
    i += sum(map(int, str(i)))
    nonSelfNum.add(i)

print(*sorted(a - nonSelfNum), sep='\n')