import sys
import math
from collections import Counter


def rounding(n):
    if n % 1 >= 0.5:
        n = math.ceil(n)
    else:
        n = math.floor(n)
    
    return n

num = []
average = 0
median = 0
mode = 0
kind = [0 for _ in range(8002)]

N = int(sys.stdin.readline())

for idx in range(N):
    num.append(int(sys.stdin.readline()))
    kind[num[idx]] += 1
    average += num[idx]
num = sorted(num)
smallnum = num[0]
bignum = num[-1]

average = rounding(average/N)
median = num[N//2]

mode = Counter(num).most_common(2)

if len(mode) > 1:
    if mode[0][1] == mode[1][1]:
        mode = mode[1][0]
    else:
        mode = mode[0][0]
else:
    mode = mode[0][0]


print(average)
print(median)
print(mode)
print(max(num) - min(num))