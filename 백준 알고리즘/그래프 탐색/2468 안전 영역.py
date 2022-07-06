import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if visited[x][y] == 1:
        visited[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = []

for k in range(max(max(arr))): # 범위를 n으로 해서 계속 틀렸음
    visited = [[1 for s in range(n)] for t in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= k:
                visited[i][j] = 0
    l = 0
    for i in range(n):
        for j in range(n):
            if dfs(i, j) == True:
                l += 1
    res.append(l)

print(max(res))
