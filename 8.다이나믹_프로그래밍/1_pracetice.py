#1149 
#RGB거리

n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
  
for i in range(1, len(p)):
    p[i][0] = p[i - 1][1] + p[i - 1][2] +  + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))