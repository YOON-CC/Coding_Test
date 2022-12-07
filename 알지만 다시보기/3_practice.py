#15654
#2_practice.py와 같은 유형의 문제이다.
#그러나 이 문제는 combination처럼 슌서를 생각하는 것이 아닌 순서를 생각 즉, (1, 2) (2, 1)을 다르게 본다.
#permutations을 기억하기 위해 기록했다.

import itertools

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []
box = list(map(int, input().split()))
box.sort()

result = list(itertools.permutations(box, m))

for i in range(len(result)):
    for s in result[i]:
        if type(s) is int:
            print(s, end=' ')
    print()