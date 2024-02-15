import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)

def bfs1(x, y):
    queue = deque()
    queue.append((x, y))
    visited1[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited1[nx][ny] and l[x][y] == l[nx][ny]:
                visited1[nx][ny] = True
                queue.append((nx, ny))

def bfs2(x, y):
    queue = deque()
    queue.append((x, y))
    visited2[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited2[nx][ny] and l2[x][y] == l2[nx][ny]:
                visited2[nx][ny] = True
                queue.append((nx, ny))

n = int(sys.stdin.readline())
l = [list(sys.stdin.readline().strip()) for _ in range(n)]
l2 = [["R" if j == "G" else j for j in i] for i in l]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

res1 = 0
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            bfs1(i, j)
            res1 += 1

res2 = 0
for i in range(n):
    for j in range(n):
        if not visited2[i][j]:
            bfs2(i, j)
            res2 += 1

print(res1, res2)
