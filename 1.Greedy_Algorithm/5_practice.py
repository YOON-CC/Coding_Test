#2195
S = input()
P = input()

cnt = 1
i = 0
index = 0
p = P[0]

while 1:
    #탈출부분 코딩
    if i == (len(P)-1):
        if p in S:
            break
        else:
            cnt+=1
            break
    
    if p in S:
        i+=1
        p += P[i]
    else:
        cnt+=1
        index = i
        p = ''
        p = P[index]
        
print(cnt)