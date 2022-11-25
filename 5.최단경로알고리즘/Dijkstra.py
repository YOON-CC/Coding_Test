#다익스트라 알고리즘
#참고
#https://velog.io/@tks7205/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-with-python
#아래 코드는 완전 기본중에 기본이다. 이미나는 이것을 알고있고 근데 문제에는 이렇게 적용되기 힘들다.
#따라서 다익스트라의 코테를 준비하기 위해서는 CLASS문제의 class_4의 3,4_practice.py를 보도록 하자!

n, m = map(int, input().split())
k = int(input())                 # 시작할 노드
INF = 1e8

graph = [[] for _ in range(n+1)] # 1번 노드부터 시작하므로 하나더 추가

distance = [INF] * (n+1)

for _ in range(m):
  u, v, w = map(int, input().split()) # u: 출발노드, v: 도착노드, w: 연결된 간선의 가중치 
  graph[u].append((v, w))             # 거리 정보와 도착노드를 같이 입력합니다.


import heapq

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # 우선순위, 값 형태로 들어간다.
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q) # 우선순위가 가장 낮은 값(가장 작은 거리)이 나온다.

    if distance[now] < dist: # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
      continue               # 따라서 다음으로 넘어간다.

    for i in graph[now]:     # 연결된 모든 노드 탐색
      if dist+i[1] < distance[i[0]]: # 기존에 입력되어있는 값보다 작다면
        distance[i[0]] = dist+i[1]   #
        heapq.heappush(q, (dist+i[1], i[0]))
dijkstra(k)
print(distance)