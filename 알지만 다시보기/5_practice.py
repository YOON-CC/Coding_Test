#15663
#https://juhee-maeng.tistory.com/91
#리스트에서 중복을 제거하는 방법을 보자!

import itertools

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []
box = list(map(int, input().split()))
box.sort()

result = list(itertools.permutations(box, m))


##중복을 제거하는 방법##
result_pro = set(result)
result = list(result_pro)
#######################

result.sort()

for i in range(len(result)):
    for s in result[i]:
        if type(s) is int:
            print(s, end=' ')
    print()