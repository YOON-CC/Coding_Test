#11725
#너비 우선 탐색을 사요한 이유는 원래 가까운 것부터 찾는 알고리즘이며 1 즉, 루트부터 시작을 하기 때문
#그래서 이전 루트를 기록해주어야 한다.
#https://velog.io/@dark6ro/%EB%B0%B1%EC%A4%80-11725%EB%B2%88-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EB%B6%80%EB%AA%A8-%EC%B0%BE%EA%B8%B0
#다시 볼만한 문제라고 생각한다.

import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a) #루트(1)의 경우 입력이 안될 수도 있기 때문이다.


queue = deque()
queue.append(1)

ans = [0]*(N+1)

def bfs():
    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if ans[nxt] == 0:
                ans[nxt] = now
                queue.append(nxt)

bfs()
res = ans[2:]
for x in res:
    print(x)