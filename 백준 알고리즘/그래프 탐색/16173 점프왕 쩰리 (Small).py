'''
dfs, bfs 둘 다 풀이 가능한데 방향이 조금 잘못 됐었음
'''

#bfs 풀이
from collections import deque

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False for j in range(n)] for i in range(n)]

dx = [1, 0]
dy = [0, 1]

def jump(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] == True
    while queue:
        x, y = queue.popleft()
        if arr[x][y] == -1:
            return 'HaruHaru'
        for i in range(2):
            nx = x + dx[i] * arr[x][y]
            ny = y + dy[i] * arr[x][y]
            if nx >= n or ny >= n:
                continue
            if visited[nx][ny] == True:
                continue
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return 'Hing'

print(jump(0, 0, visited))
