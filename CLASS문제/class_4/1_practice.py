#1043
#집합 

import sys

n, m = map(int, sys.stdin.readline().split())
true_n = set(map(int, sys.stdin.readline().split()[1:])) # 진실을 아는 사람

# set() 자료형을 통해 파티에 참여하는 사람의 번호를 입력 받는다.
party = []
for _ in range(m):
    party.append(set(map(int, sys.stdin.readline().split()[1:])))

# 파티의 수, False : 과장된 이야기, True : 진실된 이야기
cnt = [False] * m

# 파티의 수만큼 반복하여 파티에서 진실을 아는 사람이 포합되어 있는 파티를 찾는다.
for _ in range(m):
    # 각 파티에 참여한 사람을 확인
    for i, a in enumerate(party):
        # 현재 파티에 참여한 사람과 진실을 아는 사람의 교집합이 있으면
        if true_n & a:
            cnt[i] = True # 현재 파티에서는 진실을 말해야 한다.
            true_n = true_n | a # 진실을 아는 사람을 추가해준다.

print(cnt.count(False)) # 과장된 이야기를 할 수 있는 파티의 수