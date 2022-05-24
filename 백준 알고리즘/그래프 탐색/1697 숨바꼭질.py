'''
처음에 방문처리를 안해서 메모리 초과됨
'''

from collections import deque

n, k = map(int, input().split())

visited = [False] * 100001

def hide(n, k):
    queue = deque()
    queue.append([n, 0])
    visited[n] = True
    while queue:
        now, cnt = queue.popleft()
        next = [now+1, now-1, now*2]
        if now == k:
            print(cnt)
            break
        for i in next:
            if 0 <= i <= 100000 and not visited[i]:
                queue.append((i, cnt+1))
                visited[i] = True

hide(n, k)
