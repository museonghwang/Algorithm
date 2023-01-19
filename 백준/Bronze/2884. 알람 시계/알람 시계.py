H, M = map(int, input().split())
print(H, M-45) if M >= 45 else print(H-1, M+15) if H > 0 and M < 45 else print(23, M+15)