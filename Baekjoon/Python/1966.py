from collections import deque
import sys

N = int(sys.stdin.readline())

for i in range(N):
    cnt = 0
    _, n_priority = map(int, sys.stdin.readline().split())
    dq = deque(list(map(int, sys.stdin.readline().split())))

    while dq:
        maxnum = max(dq)
        left = dq.popleft()
        n_priority -= 1

        if maxnum == left:
            cnt += 1
            if n_priority < 0:
                print(cnt)
                break
        else:
            dq.append(left)
            if n_priority < 0 :
                n_priority = len(dq) - 1
