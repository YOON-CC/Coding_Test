##################
#목표가 있다면    #
#인생을 걸어라!   #
#그럼 지지 않는다.#
##################

n = int(input())

box = []
for i in range(n):
    box.append(list(map(int, input().split())))

box.sort(key = lambda x: (x[1], x[0]))

ans = end = 0
for s, e in box:
    print(s,e)