import sys
from collections import deque
input = sys.stdin.readline

def mig(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        location.append((x, y))
        country.append(popul[x][y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(popul[x][y] - popul[nx][ny]) <= r:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

def check():
    total = sum(country) // len(country)
    for x, y in location:
        popul[x][y] = total

n, l, r = map(int, input().split())
popul = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

day = 0
while True:
    visited = [[False] * n for _ in range(n)]
    move = False
    for i in range(n):
        for j in range(n):
            country = []
            location = []
            if not visited[i][j]:
                mig(i, j)
                if len(country) > 1:
                    check()
                    move = True
    if move == False:
        break
    else:
        day += 1

print(day)
