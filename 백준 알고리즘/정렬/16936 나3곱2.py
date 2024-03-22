import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
res = [[0] * 3 for _ in range(n)]

for i in range(n):
    res[i][0] = arr[i]
    while arr[i] % 2 == 0 or arr[i] % 3 == 0:
        if arr[i] % 3 == 0:
            res[i][1] += 1
            arr[i] //= 3
        if arr[i] % 2 == 0:
            res[i][2] += 1
            arr[i] //= 2

res.sort(key=lambda x: (-x[1], x[2]))

for x in res:
    print(x[0], end=" ")
