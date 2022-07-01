import sys
sys.setrecursionlimit(10 ** 6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, num):
    num += arr[x][y]
    if len(num) == 6:
        if num not in res:
            res.append(num)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        else:
            dfs(nx, ny, num)

arr = [list(input().split()) for _ in range(5)]
res = []

for i in range(5):
    for j in range(5):
        dfs(i, j, '')

print(len(res))
