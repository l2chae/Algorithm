n, m = map(int, input().split())
arr = [list(input()) for i in range(n)]

cnt = 0
for i in range(n):
    pre = '/'
    for j in range(m):
        if arr[i][j] == '-':
            if arr[i][j] != pre:
                cnt += 1
        pre = arr[i][j]

for j in range(m):
    pre = '/'
    for i in range(n):
        if arr[i][j] == '|':
            if arr[i][j] != pre:
                cnt += 1
        pre = arr[i][j]

print(cnt)
