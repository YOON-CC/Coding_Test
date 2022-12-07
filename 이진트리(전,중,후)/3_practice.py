#5639
#try, except

import sys
sys.setrecursionlimit(10**9)
nums = []
while True:                            
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break
        
def postorder(s, e):
    if s > e: 
        return
    mid = e + 1                         # 오른쪽 노드가 없을 경우

    for i in range(s+1, e+1):
        if nums[s] < nums[i]: #변화하는 루트보다 큰경우 즉, 이후 오른쪽이 된다.
            mid = i
            break

    postorder(s+1, mid-1)               # 왼쪽 확인
    postorder(mid, e)                   # 오른쪽 확인
    print(nums[s])

postorder(0, len(nums)-1)