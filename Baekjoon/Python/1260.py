import graphlib
import sys
from collections import deque 


def dfs(v):
    visited[v] = 1        
    print(v, end = " ")
    for i in range(1, n + 1):
        if visited[i] == 0 and node[v][i] == 1:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)       
    visited[v] = 1   
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n + 1):
            if visited[i] == 0 and node[v][i] == 1:
                q.append(i)
                visited[i] = 1

input = sys.stdin.readline

n, m, v = map(int, input().split())
node = [[0] * (n + 1) for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    node[n1].append(n2)

visited = [0] * (n + 1)
print(dfs(v))

visited = [0] * (n + 1)
print(bfs(v))
