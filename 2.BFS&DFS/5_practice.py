#2644
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())
s = [[] for i in range(n + 1)]
result = [0 for i in range(n + 1)]
def bfs(start):
    q = deque()
    q.append(start)
    visit = [0 for i in range(n + 1)]
    visit[start] = 1
    while q:
        d = q.popleft() # 여기서 pop해서 d에 넣는 것은 탐색하는 노드번호이다.
        for i in s[d]: #  여기서 i에 들어가는 것은 위에서 탐색하는 노드의 바로 이웃 노드들이다.
            if visit[i] == 0:
                visit[i] = 1
                result[i] = result[d] + 1
                q.append(i) 
for i in range(m):
    x, y = map(int, input().split())
    s[x].append(y)
    s[y].append(x)
print(s)

bfs(a)
print(result[b] if result[b] != 0 else -1)