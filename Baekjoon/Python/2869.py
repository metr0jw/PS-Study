from math import ceil


a, b, v = map(int, input().split())

est = (v - b) / (a - b)
print(ceil(est))
