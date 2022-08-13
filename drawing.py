import sys
input = sys.stdin.readline

N = int(input())

a = list(map(int, input().split()))

a.sort()

sum = 0
result = 0

for i in range(N):
    sum += a[i]
    result += sum

print(result)