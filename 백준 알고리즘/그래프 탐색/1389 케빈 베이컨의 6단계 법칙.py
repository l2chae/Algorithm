import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

def bfs(v):
    queue = deque()
    queue.append([v, 0])
    visited[v] = True
    while queue:
        global cnt
        now, c = queue.popleft()
        cnt += c
        for k in arr[now]:
            if not visited[k]:
                visited[k] = True
                queue.append([k, c+1])
            
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in arr:
    i.sort()

res = [0] * (n+1)

for i in range(1, n+1):
    visited = [False] * (n+1)
    cnt = 0
    bfs(i)
    res[i] = cnt

print(res.index(min(res[1:])))
