import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if l[nx][ny] == 1 and not visited[nx][ny]:
                res[nx][ny] = res[x][y] + 1
                queue.append((nx, ny))
                visited[nx][ny] = True

n, m = map(int, sys.stdin.readline().split())
l = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]
res = [[0] * m for _ in range(n)]

dest_x = 0
dest_y = 0
for i in range(n):
    for j in range(m):
        if l[i][j] == 2:
            dest_x = i
            dest_y = j
            break

bfs(dest_x, dest_y)

for i in range(n):
    for j in range(m):
        if l[i][j] == 1 and visited[i][j] == False:
            res[i][j] = -1

for row in res:
    print(" ".join(map(str, row)))
