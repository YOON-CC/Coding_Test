#12886

#10 15 35
from collections import deque

def bfs():
    global a, b, c, total, visited
    q = deque()
    q.append((a,b))
    visited[a][b] = True
    while q:
        x,y = q.popleft() #10 15 35
        z = total - x - y # 60 - 10 - 15 = 35
        if x == y == z:
            print(1)
            return
            
        for a, b in (x, y), (y, z), (x, z):
            if a < b:
                b -= a
                a += a
            elif a > b:
                a -= b
                b += b
            else:
                continue
            
            c = total - a - b
            
            x = min(a,b,c)
            y = max(a,b,c)
            
            if not visited[x][y]:
                q.append((x, y))
                visited[x][y] = True
    print(0)
    
a,b,c = map(int, input().split())

total = a + b + c

visited = [[False] * (total + 1) for _ in range(total + 1)]

if total % 3 != 0:
    print(0)
    
else:
    bfs()