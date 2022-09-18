#9082 

T = int(input())

for i in range(T):
    N = int(input())
    box = []
    cnt = 0
    star = 0

    box.append(list(map(int, input())))
    box.append(list(input()))

    for i in range(len(box[0])):
        if  i == 0:
            if box[1][i] == '*':
                box[0][0] = box[0][0] -1
                box[0][1] = box[0][1] -1
                cnt+=1
        elif i == (len(box[0])-1): 
            if box[1][i] == '*':
                box[0][i] = box[0][i] -1
                box[0][i-1] = box[0][i-1] -1
                cnt+=1   
        else:
            if box[1][i] == '*':  
                box[0][i-1] = box[0][i-1] -1             
                box[0][i] = box[0][i] -1
                box[0][i+1] = box[0][i+1] -1    
                cnt+=1  

    for i in range(len(box[0])):
        if i == (len(box[0])-1):
            if box[0][i] != 0:
                cnt +=1
            break
        
        if (box[0][i-1] == 0 or box[0][i] == 0  or box[0][i+1] == 0) and i!=0:
            continue
        
        if i == 0 and box[0][0] != 0:
            box[0][i] = box[0][i]-1
            box[0][i+1] = box[0][i+1]-1
            cnt+=1
        elif  i == 0 and box[0][0] == 0:
            continue
        else:
            box[0][i-1] = box[0][i-1]-1
            box[0][i] = box[0][i]-1
            box[0][i+1] = box[0][i+1]-1
            cnt+=1

    print(cnt)