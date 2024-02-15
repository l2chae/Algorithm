# dfs 풀이
import sys

sys.setrecursionlimit(10 ** 7)

def dfs(x, y, l, v):
    v[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not v[nx][ny] and l[x][y] == l[nx][ny]:
            dfs(nx, ny, l, v)

n = int(sys.stdin.readline())
l = [list(sys.stdin.readline().strip()) for _ in range(n)]
l2 = [["R" if j == "G" else j for j in i] for i in l]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

res1 = 0
res2 = 0
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            dfs(i, j, l, visited1)
            res1 += 1
        if not visited2[i][j]:
            dfs(i, j, l2, visited2)
            res2 += 1

print(res1, res2)

# bfs 풀이
import sys
from collections import deque

def bfs(x, y, l, v):
    queue = deque()
    queue.append((x, y))
    v[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not v[nx][ny] and l[x][y] == l[nx][ny]:
                v[nx][ny] = True
                queue.append((nx, ny))

n = int(sys.stdin.readline())
l = [list(sys.stdin.readline().strip()) for _ in range(n)]
l2 = [["R" if j == "G" else j for j in i] for i in l]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

res1 = 0
res2 = 0
for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            bfs(i, j, l, visited1)
            res1 += 1
        if not visited2[i][j]:
            bfs(i, j, l2, visited2)
            res2 += 1

print(res1, res2)
