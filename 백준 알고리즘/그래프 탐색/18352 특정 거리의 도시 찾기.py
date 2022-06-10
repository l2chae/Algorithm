from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append([v, 0])
    visited[v] = True
    while queue:
        now, cnt = queue.popleft()
        if cnt == k:
            res.append(now)
        for i in arr[now]:
            if not visited[i]:
                queue.append((i, cnt+1))
                visited[i] = True

n, m, k, x = map(int, input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

visited = [False] * (n+1)
res = []

bfs(x) # 계속 1로 해서 틀림
res.sort()

if len(res) > 0:
    for i in res:
        print(i)
else:
    print(-1)
