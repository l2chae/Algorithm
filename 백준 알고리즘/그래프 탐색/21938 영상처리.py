import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if res[x][y] == 255:
        res[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
t = int(input())

res = [[] for _ in range(n)]
for i in range(n):
    for j in range(m):
        s = sum(arr[i][j*3:j*3+3]) // 3
        if s >= t:
            res[i].append(255)
        else:
            res[i].append(0)

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1
print(cnt)
