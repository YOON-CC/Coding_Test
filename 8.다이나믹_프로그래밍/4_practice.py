#14501
#https://pacific-ocean.tistory.com/199

n = int(input())
t = []
p = []
dp = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
    
dp.append(0) #모두 기간에 충족되지 않았을 경우랑 이후 for문에서 'i+1'의 시작이 필요할 경우를 위해

for i in range(n - 1, -1, -1):
    if t[i] + i > n:# 여러 날짜와 상관없이 그냥 기간이 안되는 경우
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])#[이전값 즉 최신의 모아둔 최대값], [현재 구하는 값 + 현재 구하는값위치의 기간 이후 처음오는 값 죽 처음이란 모아둔 최대값 최신x]
print(dp[0])