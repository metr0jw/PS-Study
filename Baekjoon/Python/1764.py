import sys

no_listen = set()
no_watch = set()
n, m = map(int, sys.stdin.readline().split())

for _ in range(n):
    no_listen.add(sys.stdin.readline().rstrip('\n'))

for _ in range(m):
    no_watch.add(sys.stdin.readline().rstrip('\n'))
ans = sorted(list(no_listen & no_watch))

print(len(ans))
for out in ans:
    print(out)
    