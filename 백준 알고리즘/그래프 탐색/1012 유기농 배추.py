import sys
sys.setrecursionlimit(10 ** 6) # 재귀 최대 깊이 설정을 해줘야 함. 안그러면 런타임 에러

for i in range(int(input())):
    m, n, v = map(int, sys.stdin.readline().rstrip().split())

    arr = [[0 for j in range(m)] for i in range(n)]

    for i in range(v):
        y, x = map(int, sys.stdin.readline().rstrip().split())
        arr[x][y] = 1

    def cab(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        if arr[x][y] == 1:
            arr[x][y] = 0
            cab(x-1, y)
            cab(x, y-1)
            cab(x+1, y)
            cab(x, y+1)
            return True
        return False
    
    res = 0
    for i in range(n):
        for j in range(m):
            if cab(i, j) == True:
                res += 1
    print(res)
