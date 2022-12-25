#2529

from itertools import permutations

n = int(input())
box = list(input().split())
num_box = [0,1,2,3,4,5,6,7,8,9]
num_len = len(box)+1
result = []

select_num = list(permutations(num_box, num_len ))

for i in range(len(select_num)):
    flag = True
    for j in range(1, num_len):
        if box[j-1] == '>' and select_num[i][j-1] > select_num[i][j]:
            flag = True
        elif box[j-1] == '<' and select_num[i][j-1] < select_num[i][j]:
            flag = True
        else:
            flag = False
            break
        if j == num_len-1:
            result.append(select_num[i])

print(''.join(map(str,list(max(result)))))
print(''.join(map(str,list(min(result)))))