import sys
from queue import Queue


def bfs(graph):
    visit = [1]
    queue = Queue()

    queue.put(1)

    while queue.qsize() > 0:
        node = queue.get()
        for next_node in graph[node]:
            if next_node not in visit:
                visit.append(next_node)
                queue.put(next_node)

    return visit


num_com = int(sys.stdin.readline())
num_conn = int(sys.stdin.readline())

conn = {}
for i in range(num_com):
    conn[i+1] = set()

for i in range(num_conn):
    a, b = map(int, sys.stdin.readline().split())
    conn[a].add(b)
    conn[b].add(a)


print(len(bfs(conn)) - 1)
