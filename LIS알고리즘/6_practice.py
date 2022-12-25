#12015파이썬
#이진탐색으로 시간도 줄이고 좋네 ~
#이렇게 갱신이 가능한 것은 크기를 유지하기 때문이다.
#근데 이거는 결국에는 그 수를 나타내는 것에는 한계가 있다.
#마지막 테스트 케이스가 그런 경우이다. 
#만약 이분탐색을 사용하면서 수열을 출력을 하고싶다면 7_practice.py를 보자

# 7
# 10 20 11 15 12 13 50

# 7
# 10 20 11 1 13 14 40
import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]

LIS = [A[0]]

for item in A:
    if LIS[-1] < item:
        LIS.append(item)
        
        print("전큼", LIS) # 지워도 되지만 구현을 알기위해 적은 것
    else:
        idx = bisect_left(LIS, item)
        LIS[idx] = item
        print("전작", LIS) # 지워도 되지만 구현을 알기위해 적은 것
print(len(LIS))