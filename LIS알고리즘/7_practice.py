# 7
# 10 20 11 15 12 13 50

#14003
#이분탐색으로 가장 긴 수열의 길이와 그 수열을 출력하는 방법이다.

import bisect as bs

n = int(input())
nums = [0] + list(map(int,input().split()))
dp = [0]*(n+1)
# 문제의 조건에 음수가 포함되므로 최저를 0이 아닌 -무한대로 설정해준다.
cp = [-float('inf')]

for i in range(1, n+1):
    if nums[i] > cp[-1]:
        cp.append(nums[i])
        dp[i] = len(cp)-1
    else:
        dp[i] = bs.bisect_left(cp,nums[i])
        cp[dp[i]] = nums[i]
        
dp.remove(0)
nums.remove(0)
print(max(dp))

subsequence = [] #정답수열 입력할 배열선언
order = max(dp)  # max(dp) 값을 저장

for i in range(n - 1, -1, -1):
    if dp[i] == order:  # 만약 dp[i] 값이 order값과 같다면
        subsequence.append(nums[i])  # 해당 input_array[i]값을 추가
        order -= 1  # 해당 order 값을 1씩 감소시킨다.

subsequence.reverse()  # 큰수부터 작은수로 뽑았기 때문에
print(*subsequence) #정답수열 출력