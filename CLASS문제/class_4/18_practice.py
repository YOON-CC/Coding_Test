#12851 
#숨바꼭질 2
#이해했다. -1을 하는 이유는 제일 처음 시작할 때 의 방문 처리를 하기 위해서였다. 만약 모두 0으로 한다면
#이후의 시작점에 다시 오는 날에 방문처리가 되어있지 않기 때문이다.

from collections import deque

N, K = map(int, input().split())
MAX_SIZE = 100001

q = deque()
q.append(N)

cnt=0
check=[-1]* MAX_SIZE
check[N]=0
while q:
    x = q.popleft()
    if x==K:
        cnt+=1
    for y in [x * 2, x + 1, x - 1]:
        if 0 <= y < MAX_SIZE:
            if check[y]==-1 or check[y]>=check[x]+1: #시간: 방문한 적 없거나 현재시간 +1인경우
                check[y]=check[x]+1
                q.append(y)

print(check[K])
print(cnt)