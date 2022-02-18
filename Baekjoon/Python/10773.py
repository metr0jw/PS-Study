import sys

cog = []

for _ in range(int(sys.stdin.readline())):
    i = int(input())
    if i == 0 and len(cog):
        cog.pop()
    elif i != 0:
        cog.append(i)
print(sum(cog))
