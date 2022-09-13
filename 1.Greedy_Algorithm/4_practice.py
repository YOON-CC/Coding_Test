#2812
#이문제는 처음 입력된 숫자에서 지우고 다시 조합하는 것이아닌 순서는 그대로 두고 지워서 만드는 것이다.
N, K = map(int, input().split())
num = list(input())
k, stack = K, []

for i in range(N):
    while k > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        k -= 1
    stack.append(num[i])
print(''.join(stack[:N-K]))