import heapq # 우선순위가 높은것 부터 꺼낸다. heapq는 기본이 최소니 우서순위는 작은것 부터 깨내는 것이다.
#따라서 이를 개선하기위해 음수를 활용한다.

def heapsort(iterable):
    h=[]
    result = []
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value) # 큰양수가 -로 인해 제일 작은것으로 바뀐다.
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h)) # 따라서 큰게 작은것으로 바뀐것을 다시 원래대로 돌린다.
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)