#13549
#-1로 한 이유는 만약 숨바꼭질 1697의 문제의 경우는 어짜피 전부 +1이라서 상관이 없는데 이거는 서로 다르니 그런거

from collections import deque
import sys
input = sys.stdin.readline

MAX = 100001
N, K = map(int, input().split())
time = [-1]*MAX
time[N] = 0
q = deque()
q.append(N)
while q:
    v = q.popleft()
    if v == K: 
        print(time[v])
        break
    if 0 <= 2*v < MAX and time[2*v] == -1:
        time[2*v] = time[v]
        q.append(2*v) # 초가 0인 것이 먼저 append되어야 하니 2*v를 if문 중에서 제일 먼저 적은것이다.
    if 0 <= v-1 < MAX and time[v-1] == -1:
        time[v-1] = time[v]+1
        q.append(v-1) 
    if 0 <= v+1 < MAX and time[v+1] == -1:
        time[v+1] = time[v]+1
        q.append(v+1) 