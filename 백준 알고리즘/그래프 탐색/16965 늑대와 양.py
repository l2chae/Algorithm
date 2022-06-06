r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

flag = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'W':
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                if arr[nx][ny] == 'S':
                    flag = 0
                elif arr[nx][ny] == '.':
                    arr[nx][ny] = 'D'

print(flag)
for i in range(r):
        print(''.join(arr[i]))
