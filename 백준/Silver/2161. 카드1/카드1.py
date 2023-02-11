a = [i for i in range(1, int(input())+1)]
out = []

while len(a) > 1:
    out.append(a.pop(0))
    a.append(a.pop(0))

print(*out, *a)