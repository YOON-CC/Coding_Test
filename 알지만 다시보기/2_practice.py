#15650
#백트래킹인가 뭐 그런거 사용하는 문제인데 그냥 안하고 순서쌍및 출력 구현으로 풀었다.
#그냥 혹시 이런문제가 다음에 나오게 된다면 이런식으로 접근하려고 기록했다.

from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
box = []
result = []
for i in range(1, n+1):
    box.append(i)

result = list(combinations(box, m))

for i in range(len(result)):
    for s in result[i]:
        if type(s) is int:
            print(s, end=' ')
    print()