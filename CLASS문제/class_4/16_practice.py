#2638
#https://paris-in-the-rain.tistory.com/89
#거의 비슷하게 풀었다 ㅎㅎ 결과는 실패지만 그래도 성장하는게 느껴진다.

import sys
from collections import deque
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
n,m = map(int, sys.stdin.readline().split())
visited = [[False]*m for _ in range(n)]
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0

def outSide():
    dq = deque()
    out_visited = [[False]*m for _ in range(n)]
    dq.append((0,0))
    out_visited[0][0] = True
    board[0][0] = -1
    while dq:
        y, x = dq.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 > ny or ny >= n or 0 > nx or nx>=m: continue
            if board[ny][nx] == 1 or out_visited[ny][nx]: continue
            dq.append((ny, nx))
            board[ny][nx] = -1
            out_visited[ny][nx] = True
    return

def isMelt():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                return False
    return True

while not isMelt():
    outSide()
    check = []
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                cnt = 0
                for k in range(4):
                    ny = dy[k] + i
                    nx = dx[k] + j
                    if 0 > ny or ny >= n or 0 > nx or nx>=m: continue
                    if board[ny][nx] == -1:
                        cnt+=1
                if cnt >= 2:
                    check.append([i, j])
    for y, x in check:
        board[y][x] = 0
    answer +=1
    
print(answer)