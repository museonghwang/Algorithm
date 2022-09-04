n = int(input())

array = []
for i in range(n):
    dummy = input().split()
    array.append([dummy[0], int(dummy[1])])

def setting(data):
    return data[1]

result = sorted(array, key=setting)

for i in result:
    print(i[0], end=' ')