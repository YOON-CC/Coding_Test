#10815를 라이브러리를 사용하여 푼 문제

import bisect

n = int(input())
A = sorted(list(map(int, input().split())))

m = int(input())
B = list(map(int, input().split()))

for i in range(m):
    vigo = bisect.bisect(A, B[i])
    if B[i] == A[vigo-1]:
        print(1, end=' ')
    else:
        print(0, end=' ')