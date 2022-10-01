#https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-1202-%EB%B3%B4%EC%84%9D-%EB%8F%84%EB%91%91-Python
#1202 보석도둑

import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jew = []
for _ in range(N):
    heapq.heappush(jew, list(map(int, sys.stdin.readline().split())))  # 오름차순으로 정렬이 된다.
bags = []
for _ in range(K):
    bags.append(int(sys.stdin.readline()))
bags.sort()

answer = 0
tmp_jew = []

for bag in bags: #가방이 하나씩 꺼내진다.
    while jew and bag >= jew[0][0]: #jew 가 있고 가방과 보석의 값 비교
        # 새로운 배열에 모든 수를 -를 붙이고 힙에넣음(이러면 큰수가 제일앞에 옴)
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1]) #만약 여기서 다 빼진다고 해도 좋은거임
    if tmp_jew: #새로운 배열에 원소가 있다면 
        answer -= heapq.heappop(tmp_jew) # answer에 추가 ( -- 는 결국 +가 되니 )
    elif not jew: # jew에 원소가 없다면 여기를 실행시킨다. 
        break
print(answer)