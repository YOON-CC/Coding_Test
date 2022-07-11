#1931
n = int(input())

box = []
for i in range(n):
    box.append(list(map(int, input().split())))

box.sort(key = lambda x: (x[1], x[0])) # 람다식을 이용하여 정렬의 우선순위를 나타냄

ans = end = 0
for s, e in box: # s,e에는 하나의 배열에 첫번째, 두번째 값이 담긴다.
    if s >= end:
        ans += 1
        end = e
print(ans)
