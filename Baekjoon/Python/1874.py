import sys

def push():
    cmd.append('+')
    if len(num_to_use) > 0:
        stack.append(num_to_use.pop())
    else:
        print('NO')
        quit()

def pop():
    cmd.append('-')
    stackarray.append(stack.pop())

n = int(input())
num_to_use = [*range(n, 0, -1)]
user_array = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
stackarray = []
cmd = []

if max(user_array) > n:
        print('NO')

for i in range(n):
    while user_array != stackarray:
        if len(stack) > 0:
            if max(stack) == user_array[i]:
                pop()
                break
            else:
                push()
        else:
            push()
    
if user_array != stackarray:
    print('NO')
    quit()

for command in cmd:
    print(command)
