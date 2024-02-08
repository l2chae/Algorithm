import sys
from collections import deque

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if t[nx][ny] == 0 and not visited[nx][ny]:
                t[nx][ny] += t[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx, ny))

m, n = map(int, sys.stdin.readline().split())
t = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]

queue = deque()

for i in range(n):
    for j in range(m):
        if t[i][j] == 1:
            t[i][j] = 0
            queue.append((i, j))
            visited[i][j] = True

bfs()

day = 0
for i in t:
    if max(i) > day:
        day = max(i)

for i in range(n):
    for j in range(m):
        if t[i][j] == 0:
            if not visited[i][j]:
                day = -1

print(day)      
