#7795
#https://jinho-study.tistory.com/311
#bisectleft 들어갈 수있는 가장 좌측 인덱스
#bisectright, bisect는 들어갈 수있는 가장 우측 인덱스
import bisect

for _ in range(int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for a in A:
        cnt += (bisect.bisect(B, a-1))
    print(cnt)