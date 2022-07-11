#1931
n = int(input())

box = []
for i in range(n):
    box.append(list(map(int, input().split())))

box.sort(key = lambda x: (x[1], x[0]))

ans = end = 0
for s, e in box:
    if s >= end:
        ans += 1
        end = e
print(ans)
