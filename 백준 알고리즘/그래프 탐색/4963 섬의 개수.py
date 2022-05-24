import sys
sys.setrecursionlimit(10 ** 6) #재귀 깊이를 너무 늘리다가 런타임 에러가 남

while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break
    arr = []
    for i in range(h):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

    def island(x, y):
        if x < 0 or x >= h or y < 0 or y >= w:
            return False
        if arr[x][y] == 1:
            arr[x][y] = 0
            island(x-1, y-1)
            island(x-1, y)
            island(x-1, y+1)
            island(x, y-1)
            island(x, y+1)
            island(x+1, y-1)
            island(x+1, y)
            island(x+1, y+1)
            return True
        return False
    
    res = 0
    for i in range(h):
        for j in range(w):
            if island(i, j) == True:
                res += 1
    print(res)
