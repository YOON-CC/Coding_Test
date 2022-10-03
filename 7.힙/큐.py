from collections import deque

box = deque()

box.append(1)
box.append(2)
box.append(3)
box.append(4)
box.popleft()
box.append(5)
box.popleft()

print(box)  # 3,4,5

