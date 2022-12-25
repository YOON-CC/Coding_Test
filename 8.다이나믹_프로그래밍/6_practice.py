#11052
#점화식을 알게 되었다.
#https://www.youtube.com/watch?v=zHnM0R5at8s

n = int(input())
d = [0] * (n + 1)
p = [0] + list(map(int, input().split()))
d[1] = p[1]
for i in range(2, n + 1):
    for j in range(1, i + 1):
        if d[i] < d[i - j] + p[j]:
            d[i] = d[i - j] + p[j]
print(d[n])