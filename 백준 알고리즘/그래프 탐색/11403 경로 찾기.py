import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    for i in flag[y]:
        if not visited[i]:
            visited[i] = True
            arr[x][i] = 1
            dfs(x, i)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

flag = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            flag[i].append(j)

for i in range(n):
    visited = [False for _ in range(n)]
    dfs(i, i)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()
