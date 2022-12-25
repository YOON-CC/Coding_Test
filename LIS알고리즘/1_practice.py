#https://chanhuiseok.github.io/posts/algo-49/
#가장 긴 증가하는 부분수열

x = int(input())

arr = list(map(int, input().split()))

dp = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))