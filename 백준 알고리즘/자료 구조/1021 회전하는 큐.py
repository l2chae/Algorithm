import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
queue = deque([x for x in range(1, n+1)])

count = 0
for i in arr:
    k = queue.index(i)
    mid = len(queue) // 2
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if k <= mid:
                while queue[0] != i:
                    queue.rotate(-1)
                    count += 1
            else:
                while queue[0] != i:
                    queue.rotate(1)
                    count += 1

print(count)
