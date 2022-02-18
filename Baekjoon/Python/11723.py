import sys


S = [0 for _ in range(22)]
M = int(sys.stdin.readline())
output = []

for _ in range(M):
    user_input = sys.stdin.readline()
    if 'all' in user_input or 'empty' in user_input:
        op = user_input.rstrip('\n')
    else:
        op, num = user_input.split()
        num = int(num)

    if op == 'add':
        if S[num] == 0:
            S[num] = 1
    elif op == 'remove':
        if S[num] == 1:
            S[num] = 0
    elif op == 'check':
        if S[num] == 1:
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        if S[num] == 1:
            S[num] = 0
        else:
            S[num] = 1
    elif op == 'all':
        S = [1 for _ in range(22)]
    elif op == 'empty':
        S = [0 for _ in range(22)]
