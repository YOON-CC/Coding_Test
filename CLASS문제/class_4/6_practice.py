# 1967

from sys import stdin
from collections import deque

read = stdin.readline
V = int(read())
graph = [[] for _ in range(V+1)]

for _ in range(V-1):
    a, b, c = map(int, read().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(graph)
#bfs탐색
def bfs(start):
    visit = [-1] * (V+1)
    que = deque()
    que.append(start)
    visit[start] = 0
    _max = [0, 0]

    while que:
        t = que.popleft()
        for e, w in graph[t]:
            if visit[e] == -1:
                visit[e] = visit[t] + w
                print(visit)
                que.append(e)
                if _max[0] < visit[e]:
                    _max = visit[e], e
    return _max


dis, node = bfs(1) # 루트 노드가 들어간다.
print("")
dis, node = bfs(node)
print(dis)
