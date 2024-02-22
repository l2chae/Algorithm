import sys
from collections import deque

def bfs(x, y, c):
    queue = deque()
    queue.append((x, y, c))
    visited[x][y] = True
    while queue:
        x, y, c = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited[nx][ny] and arr[nx][ny] == "L":
                visited[nx][ny] = True
                queue.append((nx, ny, c+1))
    return c

n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == "L":
            visited = [[False] * m for _ in range(n)]
            res = max(res, bfs(i, j, 0))

print(res)
