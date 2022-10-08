import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append([home[0], home[1]])
    while q:
        x, y = q.popleft()
        if abs(x - fest[0]) + abs(y - fest[1]) <= 1000: # 편의점을 들릴 필요가 없는 경우 ㅋ
            print("happy")
            return #함수를 끝내는 부분
        for i in range(n):
            if not visited[i]: #방문 안한경우
                new_x, new_y = conv[i] # 새로운 좌표는 편의점의 좌표가 된다. 
                if abs(x - new_x) + abs(y - new_y) <= 1000:
                    q.append([new_x, new_y])
                    visited[i] = 1

t = int(input())
for i in range(t):
    n = int(input())
    home = [int(x) for x in input().split()] #출발 좌표를 넣는다.
    conv = []
    for j in range(n):
        x, y = map(int, input().split())
        conv.append([x, y]) # 편의점들의 좌표들을 넣는다.
    fest = [int(x) for x in input().split()] # 목적지의 좌표를 넣는다. 
    visited = [0 for i in range(n+1)] #home 제외
    bfs()