from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)

def bfs(v):
    queue = deque()
    queue.append([v, 1])
    visited[v] = True
    while queue:
        now, cnt = queue.popleft()
        for i in range(now, n, arr[now]):
            if not visited[i]:
                queue.append([i, cnt+1])
                visited[i] = True
                if i == b-1:
                    return cnt
        for i in range(now, -1, -arr[now]):
            if not visited[i]:
                queue.append([i, cnt+1])
                visited[i] = True
                if i == b-1:
                    return cnt
    return -1

n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())

visited = [False] * n

print(bfs(a-1))
