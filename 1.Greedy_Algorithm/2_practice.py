#2138
n = int(input())

a = input()
b = input()

now = list(map(int, a))
want = list(map(int, b))



def switch(A,B):
    L = A[:]
    press = 0
    for i in range(1, n):
        if L[i-1] == B[i-1]:
            continue
        
        press +=1 # 다른 경우 즉, 바로 위의 continue를 거치지 않음
        
        for j in range(i-1, i+2): #j의 값은 이전 현재 미래, 총 3개가 된다.
            if j<n: # 끝의 바로 이전까지 
                L[j] = 1- L[j]            
    return press if L == B else 1e9 # 인트형이 표현할 수 있는 최대의 숫자이다. 
            
#첫번째 스위치를 누리지 않을 경우
res = switch(now, want)

#첫번째 스위치를 조정해주고 시작하는 경우
now[0] = 1 - now[0]
now[1] = 1 - now[1]

res = min(res, switch(now, want) + 1)# 첫번째 스위치를 조정한 후자의 경우 1을 더해 처음의 행위를 추가

print(res if res != 1e9 else -1)
           