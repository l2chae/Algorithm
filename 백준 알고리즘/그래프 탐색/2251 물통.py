import sys
from collections import deque

def move(x, y, z):
    if not visited[x][y]:
        visited[x][y] = True
        queue.append((x, y, z))

def bfs():
    while queue:
        x, y, z = queue.popleft()
        if x == 0:
            res.append(z)
        # x -> y
        water = min(x, b-y)
        move(x-water, y+water, z)
        # x -> z
        water = min(x, c-z)
        move(x-water, y, z+water)
        # y -> x
        water = min(a-x, y)
        move(x+water, y-water, z)
        # y -> z
        water = min(y, c-z)
        move(x, y-water, z+water)
        # z -> x
        water = min(a-x, z)
        move(x+water, y, z-water)
        # z -> y
        water = min(b-y, z)
        move(x, y+water, z-water)

a, b, c = map(int, sys.stdin.readline().split())

visited = [[False] * (b+1) for _ in range(a+1)]
res = []

queue = deque()
queue.append((0, 0, c))
visited[0][0] = True

bfs()

res.sort()
for x in res:
    print(x, end=" ")
