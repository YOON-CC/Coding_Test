#2665

import sys
from heapq import heappush, heappop #힙에 이것을 넣은 이유는 검은 방때문이다. 검은방은 이후에 탐색되어야 하거나 아니어야 하기때문

input = sys.stdin.readline
n = int(input())
room = []
for _ in range(n):
    room.append(list(map(int, input().rstrip())))
visit = [[0] * n for _ in range(n)]

def dijkstra():
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    heap = []
    heappush(heap, [0, 0, 0])
    visit[0][0] = 1
    while heap:
        a, x, y = heappop(heap)
        if x == n - 1 and y == n - 1:
            print(a)                                                                          
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                if room[nx][ny] == 0: # 검은 방일 경우
                    heappush(heap, [a + 1, nx, ny])
                else: # 검은방이 아닐 경우
                    heappush(heap, [a, nx, ny])

dijkstra()