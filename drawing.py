################입력받는 준비#################
import sys

input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
#############################################

# 딕셔너리 선언
dict = {} 

############딕셔너리에서 빼는 과정#############
for w in words: # 문자열을 하나씩 뺀다.
    cnt = len(w)-1
    for ww in w: # 위에서 뺀 문자열에서 알파벳을 하나씩 뺀다.
        if ww not in dict: # 현재 딕셔너리에 없다면 (중복 방지)
            dict[ww] = pow(10, cnt) # 제곱 승으로 체운다. 
        else:
            dict[ww] += pow(10, cnt) # 이 부분이 제일 중요하다.
        cnt -= 1
print(dict)
dict = sorted(dict.values(), reverse=True) # '정렬'을 한 이후 값만 쫚뺀다.

result = 0
num = 9 

for v in dict:
    result += v*num
    num -= 1

print(result)