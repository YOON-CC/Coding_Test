#2660 
#플로이드 와샬 사용@@@@

import sys
from collections import deque
input=sys.stdin.readline
inf=sys.maxsize #간선사이즈 무한을 위한 작업

n=int(input())
arr=[[inf for _ in range(n+1)] for _ in range(n+1)] # arr무한으로 설정
for i in range(1,n+1): arr[i][i]=0

#입력받기
while 1:
   a,b=map(int,input().split())
   if a==-1:break #초반에 1로설정했으니 가능
   arr[a][b]=1
   arr[b][a]=1


for k in range(1,n+1):
   for i in range(1,n+1):
      for j in range(1,n+1):
         if arr[i][j]>arr[i][k]+arr[k][j]: #초반에 다 1로 설정했으니... 가능
            arr[i][j]=arr[i][k]+arr[k][j]

print(arr)

ans,res=[],[]
for i in range(1,n+1):
   ans.append(max(arr[i][1:n+1])) # 새로운 문법 ㅋ
   print(ans)
MIN=min(ans)
print(MIN, ans.count(MIN))
for i in range(0,n):
   if ans[i]==MIN:res.append(i+1)
print(*res)