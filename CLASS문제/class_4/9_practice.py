#9251
#https://twinw.tistory.com/126

import sys
read = sys.stdin.readline

word1, word2 = read().strip(), read().strip()
l1, l2 = len(word1), len(word2) # 6 6
cache = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < cache[j]:
            cnt = cache[j]
        elif word1[i] == word2[j]: # 같은 글자가 나올 경우
            cache[j] = cnt + 1
            
print(max(cache))