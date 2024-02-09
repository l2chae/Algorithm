import sys

n, m = map(int, sys.stdin.readline().split())
dot = []
for _ in range(m):
    y, x = map(int, sys.stdin.readline().split())
    dot.append([y, x])

mid_y = sorted(dot, key=lambda x: x[0])[m // 2][0]
mid_x = sorted(dot, key=lambda x: x[1])[m // 2][1]

res = 0
for i in range(m):
    res += abs(dot[i][0] - mid_y) + abs(dot[i][1] - mid_x)
print(res)
