import sys
from itertools import combinations
from collections import deque
import copy
input = sys.stdin.readline

def spread(s):
    count = 0
    queue = deque()
    for v in s:
        queue.append(v)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and labc[nx][ny] == 0:
                labc[nx][ny] = 2
                queue.append((nx, ny))
  
    for i in range(n):
        for j in range(m):
            if labc[i][j] == 0:
                count += 1
    
    return count

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus = []
wall = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            wall.append([i, j])
        if lab[i][j] == 2:
            virus.append((i, j))

res = 0
for i in combinations(wall, 3):
    labc = copy.deepcopy(lab)
    for j in i:
        labc[j[0]][j[1]] = 1
    res = max(res, spread(virus))

print(res)
