import sys

pwd = {}
find = []
n, m = map(int, sys.stdin.readline().split())

for _ in range(n):
    site, pw = map(str, sys.stdin.readline().split())
    pwd[site.rstrip('\n')] = pw
for _ in range(m):
    find.append(f'{sys.stdin.readline()}')

for site in find:
    print(pwd[site.rstrip('\n')])
