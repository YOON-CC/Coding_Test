#1238

#다익스트라이다. 이제는 이것을 확실하게 할때가 되었다

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

v, e, x = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))


def dijkstra(start):
    q = []
    distance = [INF] * (v + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        print(distance)
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node_index, node_cost in graph[now]:
            cost = dist + node_cost

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance


result = 0
for i in range(1, v + 1):
    go = dijkstra(i) # 반복문을 통해 노드들을 순차적으로 한 결과
    back = dijkstra(x) # 이후 바로 기존의 지정 노드
    result = max(result, go[x] + back[i]) # 이후 x, i 를 바꾸어 go에서 나온 결과의 x와 back에서의 왕복 구현

print(result)