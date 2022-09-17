#12970
import sys
input = sys.stdin.readline

n = int(input())
hw = [list(map(int, input().split())) for _ in range(n)]

hw.sort()
canHW=[]
result =0

for date in range(n, 0, -1): # 6~ 1
    while hw and hw[-1][0] >=date: # 6~ 1 ,,,,,,, hw가 남아있고 해당하는 날까지 canHW에 넣는다. 
        canHW.append(hw.pop()[1]) # 6의 점수 ~ 1의 점수 
    
    if canHW:
        canHW.sort()
        result +=canHW.pop()
print(result)
