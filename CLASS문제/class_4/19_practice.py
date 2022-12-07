#16953
#런타임에러 메모리 초과가 떴다. 어짜피 주어진 조건은 내가 거쳐왔던 길을 올 일이 없기때문에 상관없다.

from collections import deque
a,b = map(int,input().split())
q = deque()
q.append((a,1))
r = 0

def bfs():
    while(q):
        n,t = q.popleft()
        if n > b:
            continue
        if n == b:
            return print(t)
            
        q.append((int(str(n)+"1"),t+1))
        q.append((n*2,t+1))
    return print(-1)

bfs()