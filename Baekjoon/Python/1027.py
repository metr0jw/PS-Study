import sys

n = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
max_b = 0

for i in range(n):
    x = 0
    y = 0
    b_chk = 0
    for j in range(1, n - i):
        if j == 1:
            x = 1
            y = b[i + 1] - b[i]
            b_chk += 1
        elif (b[i + j] - b[i]) * x > y * j:
            x = j
            y = b[i + j] - b[i]
            b_chk += 1

    if i:
        for j in range(1, i + 1):
            if j == 1:
                x = 1
                y = b[i - 1] - b[i]
                b_chk += 1
            elif (b[i - j] - b[i]) * x > y * j:
                x = j
                y = b[i - j] - b[i]
                b_chk += 1
    max_b = max(max_b, b_chk)
    
sys.stdout.write(str(max_b))
