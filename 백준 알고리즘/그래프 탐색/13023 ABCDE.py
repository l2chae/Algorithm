import sys
sys.setrecursionlimit(10 ** 7)

def dfs(s, v, c):
    global res
    v[s] = True
    if c == 5:
        res = 1
        return
    for i in arr[s]:
        if not v[i]:
            dfs(i, v, c+1)
    v[s] = False

n, m = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * n

res = 0
for i in range(n):
    dfs(i, visited, 1)

print(res)
