# bfs 풀이
from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)

def bfs(x):
    queue = deque()
    queue.append([x, 0])
    visited[x] = True
    while queue:
        now, cnt = queue.popleft()
        if now == n-1:
            return cnt
        for i in range(arr[now]+1):
            if now+i < n:
                if not visited[now+i] and arr[now+i] != 0:
                    queue.append([now+i, cnt+1])
                    visited[now+i] = True
    return -1

n = int(input())
arr = list(map(int, input().split()))
visited = [False] * n

print(bfs(0))


# dp 풀이(기회가 된다면)
