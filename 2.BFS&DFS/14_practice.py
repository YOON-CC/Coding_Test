import sys
from collections import deque

# bfs 탐색
def bfs(v):
    queue = deque([v])
    visited[v] = 1 # 제일 처음의 수행에서 다른말로 1이 기본인데 이것을 어쩔수 없이 들어왔으니 마지막에 1을 빼주어야 한다.

    while queue:
        target = queue.popleft()

        # 주사위 눈만큼 반복한다.
        for i in range(1, 7):
            dice = target + i

            # 100칸이 넘어가면 넘긴다.
            if dice > 100:
                continue

            cnt = graph[dice]

            # 탐색하지 않은 칸이라면 탐색한다.
            if visited[cnt] == 0:
                queue.append(cnt)
                visited[cnt] = visited[target] + 1

                # 100번째 칸까지 탐색했다면 리턴
                if cnt == 100:
                    return


n, m = map(int, sys.stdin.readline().split())

# 보드판을 표현, 사다리나 뱀인 경우에는 이동 후 좌표로 표시
graph = [i for i in range(101)]
for _ in range(n + m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] = b

# 탐색한 칸까지 가기 위한 주사위 던진 횟수를 체크
visited = [0] * 101

# 1번 칸부터 bfs 탐색
bfs(1)

# 100번째 칸까지 가기 위한 주사위 던진 횟수에서
# 1번 칸에서 카운트한 주사위 던진 횟수를 빼준다.
print(visited[100] - 1)