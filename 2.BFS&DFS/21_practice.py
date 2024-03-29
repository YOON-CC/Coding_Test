#11559

from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# bfs알고리즘 시작
def bfs(i, j, char):
    q = deque()
    q.append([i, j])
    chain.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 12 and 0 <= ny < 6 and visit[nx][ny] == 0 and s[nx][ny] == char:
                visit[nx][ny] = 1
                q.append([nx, ny])
                chain.append([nx, ny])

#
def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if s[j][i] != "." and s[k][i] == ".":
                    s[k][i] = s[j][i]
                    s[j][i] = "."
                    break
                
# 이제 입력값 받기
s = [list(input().strip()) for i in range(12)]
result = 0

#작동이 시작되는 자리
while True:
    isTrue = False
    visit = [[0] * 6 for i in range(12)] # 방문여부
    for i in range(12):
        for j in range(6):
            if s[i][j] != "." and visit[i][j] == 0: # 초반 조건!
                visit[i][j] = 1
                chain = []
                bfs(i, j, s[i][j])
                if len(chain) > 3:
                    isTrue = True
                    for x, y in chain: s[x][y] = "."
    if not isTrue: break # 반복문 탈출 => 탈출하는 경우는 더이상 맞출것이 없는 경우이다.
    down()
    result += 1
print(result)