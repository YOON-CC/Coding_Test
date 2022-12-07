#9465
#이런 유형은 한정되어있기때문에 차라리 코드를 외우는게 좋을 수도 있다.

# 50 10 100 20 40
# 30 50  70 10 60

t = int(input())
for i in range(t):
  s = []
  n = int(input())
  for k in range(2):
    s.append(list(map(int, input().split())))
  for j in range(1, n):
    if j == 1: 
      s[0][j] += s[1][j - 1]
      s[1][j] += s[0][j - 1]
    else:
      s[0][j] += max(s[1][j - 1], s[1][j - 2])
      s[1][j] += max(s[0][j - 1], s[0][j - 2])
  print(max(s[0][n - 1], s[1][n - 1]))