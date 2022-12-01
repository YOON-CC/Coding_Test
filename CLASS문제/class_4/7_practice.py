#2096
#슬라이싱 윈도우
#DP에서 말하는 슬라이딩 윈도우 기법이란, 메모이제이션을 할 때 더 이상 사용하지 않는 값을 저장하지 않고 배열을 계속하여 갱신해주는 것을 의미한다.

import sys
input = sys.stdin.readline

n = int(input())
tmp = list(map(int,input().split()))
dp1 = tmp; dp2 = tmp
for _ in range(n-1):
    a,b,c = map(int,input().split())
    # dp배열에 append 하는 것이 아니라, 값을 갱신시켜준다.
    dp1 = [a+max(dp1[0],dp1[1]),b+max(dp1),c+max(dp1[1],dp1[2])]
    dp2 = [a+min(dp2[0],dp2[1]),b+min(dp2),c+min(dp2[1],dp2[2])]
print(max(dp1),min(dp2))