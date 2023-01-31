import sys
m = int(sys.stdin.readline())
S = 0b0
all_S = 0b111111111111111111111
not_S = 0b000000000000000000000

for i in range(m):
    cmd = sys.stdin.readline().rstrip().split(" ")
    if cmd[0] == 'add':
        S |= 1 << int(cmd[-1])
    elif cmd[0] == 'remove':
        S &= ~(1 << int(cmd[-1]))
    elif cmd[0] == 'check':
        if S & (1 << int(cmd[-1])):
            sys.stdout.write('1\n')
        else:
            sys.stdout.write("0\n")
    elif cmd[0] == 'toggle':
        S ^= 1 << int(cmd[-1])
    elif cmd[0] == 'all':
        S = S | all_S
    elif cmd[0] == 'empty':
        S = S & not_S