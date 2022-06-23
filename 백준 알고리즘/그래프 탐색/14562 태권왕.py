from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)

def bfs(s, t):
    queue = deque()
    queue.append([s, t, 0])
    while queue:
        now_m, now_o, cnt = queue.popleft()
        if now_m == now_o:
            return cnt
        if now_m <= now_o: # now_m이 큰 경우는 고려할 필요가 없으므로(이부분이 없으면 메모리 초과 발생)
            queue.append((now_m*2, now_o+3, cnt+1))
            queue.append((now_m+1, now_o, cnt+1))

for i in range(int(input())):
    s, t = map(int, input().split())
    print(bfs(s, t))
