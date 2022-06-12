from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def bfs(s):
    global cnt
    queue = deque([s])
    visited[s] = True
    while queue:
        v = queue.popleft()
        res[v] = cnt
        cnt += 1
        for i in arr[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, r = map(int, input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(n):
    arr[i+1].sort()

visited = [False] * (n+1)
res = [0] * (n+1)
cnt = 1

bfs(r)

for i in range(1, n+1):
    print(res[i])
