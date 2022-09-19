#2036
#코드는 맞는데 왜 반례가 있는줄 모르겠다. 분발하자

import sys
input = sys.stdin.readline


def getMaxScore(nums, N):
    if N == 1:
        return nums[0]

    score = 0

    # 음수
    for i in range(0, N-1, 2):
        cur, next = nums[i], nums[i+1]

        if cur < 0 and next < 0:
            score += cur * next
        else:
            if cur < 0 and next > 0:
                score += cur
            break

    # 전부 음수이면서 N이 3이상 홀수일 때의 반례
    if i+2 == N-1:
        if nums[N-1] < 0:
            score += nums[N-1]

    # 양수
    addPoint = 0
    for i in range(N-1, 0, -2):
        cur, next = nums[i], nums[i-1]

        if cur > 1 and next > 1:
            score += cur * next
        else:
            addPoint = i
            break

    # 나머지 양수들 더하기
    for i in range(addPoint, -1, -1):
        if nums[i] >= 1:
            score += nums[i]
        else:
            break

    return score


if __name__ == '__main__':
    N = int(input())
    nums = [int(input()) for _ in range(N)]

    nums.sort()

    maxScore = getMaxScore(nums, N)
    print(maxScore)
    
    
# 2036

# # 큰거 두개를 곱하거나
# # => 두 개 모두가  음수들 중 큰 것들, 두 개 모두 양수들 중 큰 것들
# # 하나를 뽑거나
# # => 이러한 경우는 max로 간단히
# # 이 두가지 경우 중에서 큰것
# # 그리고 0의 예외상황을 만들어야 한다.

# n = int(input())
# box = []

# for i in range(n):
#     box.append(int(input()))

# box.sort()

# who_is_the_best = 0
# result = 0

# if len(box) > 2: 
#     while box:
#         if len(box) < 3:
#             break
#         a1 = 0
#         a2 = 0
#         b = 0
            
#         a1 = box[0]*box[1] 
#         a2 = box[len(box)-1]*box[len(box)-2] 
#         b = box[-1] 
        
#         if a2 == b:
#             who_is_the_best = b
#             del box[-1]
#         else:
#             who_is_the_best = max(a1,a2,b)
#             if who_is_the_best == a1:
#                 del box[0]
#                 del box[0]
#             elif who_is_the_best == a2:
#                 del box[len(box)-1]
#                 del box[len(box)-1]
#             else:
#                 del box[-1]
#         result+=who_is_the_best


# if len(box) ==2:
#     a = box[0]*box[1]
#     b = box[1]
    
#     who_is_the_best = max(a,b) 
#     result+=who_is_the_best

#     if (who_is_the_best == b) and a != 0:
#         result+=box[0]
# else:
#     result+=box[0]
    
# print(result)
