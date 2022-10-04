#2667
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, a, b):
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


# 그래프 입력받는 부분
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#DFS적용하는 부분, 단지는 구분이 되어져 있기때문에 1을 찾아야 한다. 1을 찾으면 DFS를 바로 실행을 하고 모두 0으로 만들어 버린다.
cnt = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt.append(bfs(graph, i, j))


#결과 출력 부분
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])