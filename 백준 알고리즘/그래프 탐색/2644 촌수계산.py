from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
n1, n2 = map(int, input().split())
arr = [[] for i in range(n+1)]
for i in range(int(input())):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

for i in range(n):
    arr[i+1].sort()

res = [False] * (n+1)
def bfs(v, k): # n1, n2
    queue = deque()
    queue.append([v, 0]) # n1, cnt
    res[v] = True # 변수 바꾸면 꼭 확인
    while queue:
        now, cnt = queue.popleft()
        if now == k:
            return cnt
        for i in arr[now]:
            if not res[i]:
                queue.append((i, cnt+1))
                res[i] = True
    return -1

print(bfs(n1, n2))
