#2589
#이번 문제는 브루트포스를 섞은 문제이다. 보물 2개중 하나가 무조건 보물이라 기준을 잡고 최댓값을 잡는 것이다.

from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(i, j):
    q = deque()
    q.append([i, j])
    max_n = 0
    while q:
        a, b = q.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < m and visit[x][y] == 0 and s[x][y] != "W": # 들어와도 되는 조건 
                visit[x][y] = 1
                s[x][y] = s[a][b] + 1
                max_n = max(max_n, s[x][y])
                q.append([x, y])
    return max_n
n, m = map(int, input().split())
s = []
result = 0
for i in range(n):
    s.append(list(input().strip())) # 표넣는 과정
    
for i in range(n):
    for j in range(m):
        if s[i][j] != "W": # 욱지라면
            visit = [[0] * m for _ in range(n)] # 방문 시작(매번 갱신이 된다.)
            s[i][j] = 0 # 기준으로 시작된다. 0에서 계속 증가가됨
            visit[i][j] = 1
            result = max(result, bfs(i, j))
print(result)