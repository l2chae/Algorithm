import sys
import heapq
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort(key=lambda x:x[0])

end = [0]
cnt = 1
for s, e in time:
    if s >= end[0]:
        heapq.heappop(end)
    else:
        cnt += 1
    heapq.heappush(end, e)

print(cnt)
