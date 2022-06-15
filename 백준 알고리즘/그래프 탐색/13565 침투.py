import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if x < 0 or x >= m or y < 0 or y >= n:
        return
    if arr[x][y] == 0:
        arr[x][y] = 2
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)

m, n = map(int, input().split())
arr = []
for i in range(m):
    arr.append(list(map(int, input())))

for i in range(n):
    if arr[0][i] == 0:
        dfs(0, i)

# Yes, No로 해서 한참 헤맸음;;
if 2 in arr[-1]:
    print('YES')
else:
    print('NO')
