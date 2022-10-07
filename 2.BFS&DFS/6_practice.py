#1697
from collections import deque

def bfs():
    q = deque()
    q.append(N)
    while q:
        v = q.popleft()
        if v == K: 
            print(time[v])
            return
        for next_step in (v-1, v+1, v*2):
            if 0 <= next_step < MAX and not time[next_step]: # not time[next_step]이것은 방문하지 않았다면 이다.!
                time[next_step] = time[v] + 1
                q.append(next_step) # 여기서 v-1, v+1, v*2를 append하는 순서는 상관이 없다. 어짜피 9번줄에서 찾아낼거니

MAX = 100001
N, K = map(int, input().split())
time = [0]*MAX
bfs()