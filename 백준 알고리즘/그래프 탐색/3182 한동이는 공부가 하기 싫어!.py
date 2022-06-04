import sys
sys.setrecursionlimit(10 ** 6)

def dfs(v, c):
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            c = dfs(i, c+1)
    return c

n = int(input())
arr = [[] for i in range(n+1)]
for j in range(n):
    arr[j+1].append(int(input()))

res = [0] * (n+1)
for i in range(1, n+1):
    visited = [False] * (n+1)
    res[i] = dfs(i, 1)
print(res.index(max(res)))
