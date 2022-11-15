import heapq

heap = []

# 아래 for문을 실행하고 나면 heap은 [-5,-4,-3,-2,-1]로 힙 정렬이 되게 된다.
for i in range(1,6):
	heapq.heappush(heap, -i) 
 
# [-5,-4,-3,-2,-1]로 된 것이 -가 때지면서 5,4,3,2,1 이렇게 출력된다.
for i in range(5):
	print(-heapq.heappop(heap))