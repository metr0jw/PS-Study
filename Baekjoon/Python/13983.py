import sys


def dist(a, b, c):
    r = 1.0
    for i in range(c):
        r = r * (a - i) / (b - i)

k, r = map(int, sys.stdin.readline().split())
b=(1<<k)-r+1
