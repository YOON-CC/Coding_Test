#11509

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 현재 떠있는 화살의 개수를 나타낸다. 공간 복잡도는 O(n), O(100만)
# floating[height]=arrow_count. 즉, 높이 height의 떠있는 중인 화살의 현재 개수를 뜻한다.

# [0]*(n+1)인 경우, 인덱스 에러가 난다. 당연하게도 높이는 최대 1000000까지이기 때문이다.
# 만약 n = 5이고 그 중 높이가 1000000이라면 floating[1000000]에 의해 인덱스 에러가 난다.
floating = [0] * 1000001

# O(n) 풀이
for height in arr:
    # 해당 높이에서 떠 있는 화살이 있다면,
    if floating[height] > 0:
        # 그 화살 중 하나를 바로 아래 높이로 이동시킨다.
        floating[height] -= 1
        floating[height - 1] += 1
    # 해당 높이에서 떠 있는 화살이 없다면, 화살을 쏜다. 일단, 맞췄으니까 바로 높이를 -1한다.
    else:
        floating[height - 1] += 1

# 남아 있는 화살의 총합이 답이다. o(n)
print(sum(floating))