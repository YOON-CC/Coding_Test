#2468
from collections import deque
 
n = int(input())
graph = []
maxNum = 0
 
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j] # 여기서 maxNum이 결정이 된다.

#표할때 국룰!  
dx = [0 ,0, 1, -1]
dy = [1, -1, 0 ,0]

############bfs함수적용############
def bfs(a, b, value, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1
 
    while q:
        x, y = q.popleft()
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n: # 하나의 경우에 대해 상하좌우를 탐색하는 경우이다.
                if graph[nx][ny] > value and visited[nx][ny] == 0: #만약 상하좌우가 비고다 높고 방문 안했으면
                    visited[nx][ny] = 1 # 방문 처리를 해주고 
                    q.append((nx, ny)) # 넣어준다. 이는 침수된 지역은 넣지 않으니 while q:를 종료하여 끝을 내는 것을 가져옴
 
result = 0
############bfs함수적용############
for i in range(maxNum):
    visited = [[0] * n for i in range(n)] #방문여부는 비의 높이가 새로 바뀔때 마다 항상 초기화가 된다.
    cnt = 0
 
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0: # 브루트포스 식으로 하나씩 다 보면서 새 경계를 찾는 느낌으로 진행
                bfs(j, k, i, visited)
                cnt += 1 # 카운트가 이렇게 되는 이유는 영역의 수이다. 한칸이 아닌 구분된 영역!

    if result < cnt:
        result = cnt
 
print(result)

# 비의 양에따라 테스트 다른 평해 세계이니 visit는 초기화가 되어야한다.
# 각 양에 따라 처음부터 끝까지 브루트포스 식으로 탐색을 하다가 비에 잠기지 않는 곳을 발견한다면 bfs시도
# 만약 침수된 지역이 있다면 상하좌에서 침수된 지역이 존재를 한다면 q에 못넣고 그게 모든 방향이라면 bfs종료
# 다시 침수안된 지역을 브루트포스로 찾다가 이전의 bfs에서 못다한 부분이 있다면 시도!
# 이런식으로 구분을 치면서 계속 찾는다.