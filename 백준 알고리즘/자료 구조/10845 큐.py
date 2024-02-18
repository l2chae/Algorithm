import sys
from collections import deque

n = int(sys.stdin.readline())
l = [sys.stdin.readline().strip() for _ in range(n)]

queue = deque()

for x in l:
    if "push" in x:
        queue.append(int(x.split()[1]))
    elif x == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif x == "size":
        print(len(queue))
    elif x == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif x == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)
