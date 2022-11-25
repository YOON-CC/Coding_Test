#1504 파이썬

import heapq
import sys
input = sys.stdin.readline
n, e = map(int, input().split())
s = [[] for i in range(n + 1)]
inf = sys.maxsize
for i in range(e):
    a, b, c = map(int, input().split())
    s[a].append([b, c])
    s[b].append([a, c])
v1, v2 = map(int, input().split())


def dijkstra(start):
    dp = [inf for i in range(n + 1)]
    q = []
    heapq.heappush(q, (0, start)) # 우선순위, 값 형태로 들어간다.
    dp[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 우선순위가 가장 낮은 값(가장 작은 거리)이 나온다.

        if dp[now] < dist: # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
            continue               # 따라서 다음으로 넘어간다.

        for i in s[now]:     # 연결된 모든 노드 탐색
            if dist+i[1] < dp[i[0]]: # 기존에 입력되어있는 값보다 작다면
                dp[i[0]] = dist+i[1]   #
                heapq.heappush(q, (dist+i[1], i[0]))
    return dp            

one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
cnt = min(one[v1] + v1_[v2] + v2_[n], one[v2] + v2_[v1] + v1_[n])
print(cnt if cnt < inf else -1)