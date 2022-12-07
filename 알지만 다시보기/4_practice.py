#15652
#combinations_with_replacement라는 것을 사용했다.
#이는 조합과는 달리 중복조합을 의미한다.
#https://juhee-maeng.tistory.com/91

from itertools import combinations_with_replacement

n , m = map(int, input().split())
box = []
for i in range(1, n+1):
    box.append(i)

for cwr in combinations_with_replacement(box, m):
    for s in cwr:
        if type(s) is int:
            print(s, end=' ')
    print()
    
