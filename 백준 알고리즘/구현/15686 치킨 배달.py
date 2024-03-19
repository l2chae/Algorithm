import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

house = []
chicken = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append([i, j])
        if arr[i][j] == 2:
            chicken.append([i, j])

result = 9999
for i in combinations(chicken, m):
    total = 0
    for k in house:
        chicken_len = 9999
        for j in i:
            chicken_len = min(chicken_len, abs(k[0]-j[0]) + abs(k[1]-j[1]))
        total += chicken_len
    result = min(result, total)

print(result)
