import sys


input = sys.stdin.readline
n, m, b = map(int, input().split())
gnd = []
total = 0
res_h = -1
res_t = sys.maxsize

for i in range(n):
    temp = list(map(int, input().split()))
    gnd.append(temp)
min = min(min(gnd))
max = max(max(gnd))

for h in range(max, min-1, -1):
    cmp = 0
    rmv = 0
    add = 0
    for row in gnd:
        for i in row:
            cmp += h - i
            if h - i > 0:
                add += h - i
            else:
                rmv += h - i
    if abs(rmv*2)+add < res_t and add <= b:
        res_h = h
        res_t = abs(rmv*2)+add

print(f'{res_t} {res_h}')

