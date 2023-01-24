a = set(range(1, 10000))
a_remove = set()

for num in a:
    for n in str(num):
        num += int(n)
    a_remove.add(num)

for num in sorted(a-a_remove):
    print(num)