#19598

import sys
input = sys.stdin.readline
import heapq


N = int(input())

schedules = sorted([list(map(int, input().split())) for _ in range(N)])
h = []

for s, e in schedules:
    if h and h[0] <= s:
        heapq.heappop(h)
    heapq.heappush(h,e)

print(len(h))