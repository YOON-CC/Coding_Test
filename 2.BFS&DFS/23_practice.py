#5427

from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():
    while q:
        x, y = q.popleft()
        #처음에는 불로 바로 시작하게 되어진다.
        if visited[x][y] != "FIRE": 
            flag = visited[x][y]
        else:
            flag = "FIRE"

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w: # 떨어지지 않은 경우
                if visited[nx][ny] == -1 and (board[nx][ny] == "." or board[nx][ny] == "@"):
                    #불일경우
                    if flag == "FIRE": 
                        visited[nx][ny] = flag
                    #상근일 경우
                    else: 
                        visited[nx][ny] = flag + 1
                    #불부터 시작해서 상근 불 상근 이렇게 번갈아 가진다.
                    q.append((nx, ny))
            else: # 떨어진 경우
                if flag != "FIRE": # flag는 끝자락으로 도착하니 ..
                    return flag + 1

    return "IMPOSSIBLE"


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        w, h = map(int, input().split())
        q = deque()
        board = []
        visited = [[-1] * w for _ in range(h)] # 방문여부
        for i in range(h):
            board.append(list(input().strip()))
            for j in range(w):
                if board[i][j] == "@":
                    visited[i][j] = 0
                    start = (i, j)
                elif board[i][j] == "*":
                    visited[i][j] = "FIRE"
                    q.append((i, j)) 
#불을 먼저 넣는다. q에다가 그리고 밑에처럼 이후에 사람위치를 넣는다 
        q.append(start)
        print(bfs())
