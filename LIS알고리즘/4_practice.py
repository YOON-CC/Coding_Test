#내가만든문제
#가장 긴 증가하는 수열의 합

import sys

n = int(sys.stdin.readline().strip())
a = [int(x) for x in sys.stdin.readline().split()]
dp = a[:]
dp_1 = [1 for i in range(n)]


for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + a[i])


for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp_1[i] = max(dp_1[i], dp_1[j]+1)

print(dp[dp_1.index(max(dp_1))])


