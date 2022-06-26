# 깊이와 방문순서를 착각해서 틀린 문제

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(s, c):
    visited[s] = True
    res[s] = c
    for k in arr[s]:
        if not visited[k]:
            dfs(k, c+1)

n, m, r = map(int, input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(n):
    arr[i].sort()

visited = [False] * (n+1)
res = [-1] * (n+1)

dfs(r, 0)

for i in range(1, n+1):
    print(res[i])
