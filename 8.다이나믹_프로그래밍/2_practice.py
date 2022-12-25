#1309
#https://pacific-ocean.tistory.com/211
#이 문제는 점화식을 찾아도 되고~ 근데 여기 코드는 점화식을 쓰지 않았다.

n = int(input())
s = [[0] * 3 for i in range(100001)]
for i in range(3):
    s[1][i] = 1
for i in range(2, 100001):
    s[i][0] = s[i - 1][1] + s[i - 1][2] % 9901
    s[i][1] = s[i - 1][0] + s[i - 1][2] % 9901
    s[i][2] = s[i - 1][0] + s[i - 1][1] + s[i - 1][2] % 9901
print(sum(s[n]) % 9901)