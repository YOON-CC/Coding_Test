#9935파이썬
#이런 문제는 틀리면 안된다. 정신차리자

n = input()
m = input()

stack = []

for c in n:
    stack.append(c)
    if ''.join(stack[-len(m):]) == m:
        del stack[-len(m):]

ans = ''.join(stack)
if ans == '':
    print("FRULA")
else:
    print(ans)