# 정말 계속 틀린 문제... 함수 구현에서 순서 문제인듯한데...

import sys
sys.setrecursionlimit(10 ** 6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    visited[x][y] = True
    if arr[x][y] == 'P':
        cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if arr[nx][ny] != 'X':
                dfs(nx, ny)

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[False for j in range(m)] for i in range(n)]

cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'I':
            dfs(i, j)

if cnt:
    print(cnt)
else:
    print('TT')
