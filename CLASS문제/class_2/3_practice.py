#11050

#이항계수

from math import factorial
n, k = map(int, input().split())
b = factorial(n) // (factorial(k) * factorial(n - k))
print(b)