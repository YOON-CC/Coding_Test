#https://claude-u.tistory.com/208
#12865
#내가 이문제를 그리디랑 존나게 당황한 이유는 보석 도둑 그리디 문제 같은 경우는 가방에 하나만 담을수 있다.

import sys

N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))


#냅색 문제 풀이
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0] 
        value = stuff[i][1]
        
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])
        # print(knapsack)
        # print("j :", j, " weight :", weight, " value :", value)
        # print()
print(knapsack[N][K])