import sys

n, m = map(int, sys.stdin.readline().split())
l = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

res = 0
for i in l:
    res += sum(i) * 6

for i in l:
    for j in i:
        if j > 1:
            res -= (j-1) * 2

for i in range(n):
    for j in range(m):
        if (i == 0) and (j != m-1):
            res -= min(l[i][j], l[i][j+1]) * 2
        elif i != 0:
            if j != m-1:
                res -= (min(l[i][j], l[i-1][j]) * 2 + min(l[i][j], l[i][j+1]) * 2)
            else:
                res -= min(l[i][j], l[i-1][j]) * 2

print(res)
