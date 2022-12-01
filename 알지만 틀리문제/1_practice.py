#부경대 코테에 나왔다.
#최종적으로 풀었지만 순발력이 부족했다.

from collections import deque
import sys

input = sys.stdin.readline


n, m ,s = map(int, input().split())

box = list(map(int, input().split()))
graph = [[]*n for _ in range(n+1)]
visited = [0]*(m+1)
result = 0
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b) # 문제가 양방향으로 이동할수 있다고 하였기 때문에 이렇게 적은것
    graph[b].append(a)
    
def bfs(start):
    queue = deque([start])
    global cnt
    visited[start] = 1
    fix = box[start-1]
    while queue:
        v = queue.popleft()            
        for i in graph[v]:
            if not visited[i] and (fix == box[i-1]):
                queue.append(i)
                visited[i] = True
                cnt+=1
    return cnt  
       
cnt = 1
visited = [0]*(m+1)
bfs(s)
result = max(result, cnt)
print(cnt)
