import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    res[s] = 0
    while q:
        cost, now = heapq.heappop(q)
        if res[now] < cost:
            continue
        for i in city[now]:
            total = cost + i[1]
            if total < res[i[0]]:
                res[i[0]] = total
                heapq.heappush(q, (total, i[0]))

n = int(input())
m = int(input())
city = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    city[s].append((e, c))
s, e = map(int, input().split())

res = [INF] * (n+1)

dijkstra(s)

print(res[e])
