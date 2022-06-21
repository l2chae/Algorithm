from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
queue = deque()

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx, ny))

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append((i, j))
bfs()

res = 0
for i in range(n):
    for j in range(m):
        res = max(res, arr[i][j])
print(res-1)
