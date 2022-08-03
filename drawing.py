##################
#목표가 있다면    #
#인생을 걸어라!   #
#그럼 지지 않는다.#
##################

n,k = map(int, input().split())

box = []
cnt = 0
a = 0
result = 0

for i in range(n):
    box.append(int(input()))

box.sort()
box.reverse()

for i in range(n):
    cnt += k//box[i]
    k %=box[i]
        
print(cnt)