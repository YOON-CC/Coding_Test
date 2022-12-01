#음수간선이 존재할때 쓰는 알고리즘
#다익스트라와 비교되지만 벨만 포드는 음스간선까지 가능하다. 그래서 음수간선 문제(텔포)등은 이거!
#다익스트라보다 시간의 복잡도가 크다. ㅠ
#https://velog.io/@kimdukbae/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B2%A8%EB%A7%8C-%ED%8F%AC%EB%93%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Bellman-Ford-Algorithm
#https://www.youtube.com/watch?v=Ppimbaxm8d8
#https://velog.io/@younge/Python-%EC%B5%9C%EB%8B%A8-%EA%B2%BD%EB%A1%9C-%EB%B2%A8%EB%A7%8C-%ED%8F%AC%EB%93%9CBellman-Ford-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
#https://lackofwillpower.tistory.com/25
#https://4legs-study.tistory.com/26
#최종적으로는 마지막 링크를 보고 이해를 했다.
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수를 입력
v, e = map(int, input().split())
# 모든 간선에 대한 정보를 담는 리스트 만들기
edges = []
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (v + 1)

# 모든 간선의 정보 입력
for _ in range(e):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미 (a -> b 의 비용이 c)
    edges.append((a, b, c))


def bellman_ford(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    # 전체 v - 1번의 라운드(round)를 반복
    for i in range(v):
        # 매 반복마다 '모든 간선'을 확인한다.
        for j in range(e):
            cur_node = edges[j][0] #출발노드
            next_node = edges[j][1] #도착노드
            edge_cost = edges[j][2] #가중치
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            # INF라는 조건은 내가 입력한 제일 처음~ 시작점(START)을 찾는 조건이다.
            # 처음에 이거를 몰랐던 이유는 그래프는 어떻게든 연결이 되어있다는 사실을 파악못함
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                # v번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == v - 1:
                    return True

    return False


# 벨만 포드 알고리즘 수행
negative_cycle = bellman_ford(1)

# 음수 순환이 존재하면 -1 출력
if negative_cycle:
    print("-1")
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리를 출력
    for i in range(2, v + 1):
        # 도달할 수 없는 경우, -1 출력
        if distance[i] == INF:
            print("-1")
        # 도달할 수 있으면 거리 출력
        else:
            print(distance[i])