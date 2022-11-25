#7662

#이중 큐

import heapq

t = int(input())

for i in range(t):
    k = int(input())
    q1, q2 = [], []
    visited = [False] * k

    for j in range(k):
        com, num = input().split()

        if com == 'I':
            heapq.heappush(q1, (int(num), j))
            heapq.heappush(q2, (-int(num), j))
            visited[j] = True 

        else: # D가 입력된 경우이다.
            if num == '1': # 최대값 그리고 최대값을 뺄때 원래 -를 붙이지만 여기서는 보여주는 것이아닌 그냥 삭제니 안해도 무관
                while q2 and not visited[q2[0][1]]:
                    heapq.heappop(q2)
                if q2:
                    visited[q2[0][1]] = False
                    heapq.heappop(q2)
            else: # 최소값
                while q1 and not visited[q1[0][1]]:
                    heapq.heappop(q1)
                if q1:
                    visited[q1[0][1]] = False
                    heapq.heappop(q1)

    while q1 and not visited[q1[0][1]]:
        heapq.heappop(q1)
    while q2 and not visited[q2[0][1]]:
        heapq.heappop(q2)

    if not q1 or not q2: # 아무것도 없을경우
        print("EMPTY")
    else: # 그냥 출력하는 부분
        a = -q2[0][0] # 이제는 보여주어야 하니 -를 붙여서 나온다.
        b = q1[0][0]
        print("%d %d" % (a, b))