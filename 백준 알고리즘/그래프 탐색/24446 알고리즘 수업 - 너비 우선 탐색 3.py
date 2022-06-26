from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def bfs(s, c):
    queue = deque()
    queue.append([s, c])
    visited[s] = True
    while queue:
        now, cnt = queue.popleft()
        res[now] = cnt
        for i in arr[now]:
            if not visited[i]:
                queue.append((i, cnt+1))
                visited[i] = True

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

bfs(r, 0)

for i in range(1, n+1):
    print(res[i])
