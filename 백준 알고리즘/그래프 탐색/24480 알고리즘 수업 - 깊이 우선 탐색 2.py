import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(s):
    global cnt
    visited[s] = True
    res[s] = cnt
    cnt += 1
    for k in arr[s]:
        if not visited[k]:
            dfs(k)

n, m, r = map(int, input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(n):
    arr[i+1].sort(reverse=True)

visited = [False] * (n+1)
res = [0] * (n+1)
cnt = 1

dfs(r)

for i in range(1, n+1):
    print(res[i])
