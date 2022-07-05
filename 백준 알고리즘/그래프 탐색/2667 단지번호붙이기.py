def dfs(x, y):
    global k
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if arr[x][y] == 1:
        k += 1
        arr[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
res = []

cnt = 0
for i in range(n):
    for j in range(n):
        k = 0
        if dfs(i, j) == True:
            cnt += 1
            res.append(k) # 이부분을 함수 안에 넣어서 헤맸던 문제
res.sort()

print(cnt)
for i in res:
    print(i)
