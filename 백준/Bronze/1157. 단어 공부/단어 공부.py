dummy = input()

a = [dummy.upper().count(chr(i)) for i in range(65, 91)]
print('?' if a.count(max(a)) > 1 else chr(a.index(max(a)) + 65))