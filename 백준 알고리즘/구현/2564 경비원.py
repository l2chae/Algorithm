import sys

x, y = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dd, dl = map(int, sys.stdin.readline().split())

res = 0
for i in range(n):
    d = arr[i][0]
    l = arr[i][1]
    if {d, dd} == {1, 2}:
        res += y + min(l + dl, x * 2 - l - dl)
    elif {d, dd} == {3, 4}:
        res += x + min(l + dl, y * 2 - l - dl)
    elif {d, dd} == {1, 3}:
        res += l + dl
    elif {d, dd} == {2, 3}:
        if d == 3:
            res += y - l +dl
        else:
            res += y - dl + l
    elif {d, dd} == {1, 4}:
        if d == 1:
            res += x - l + dl
        else:
            res += x - dl + l
    elif {d, dd} == {2, 4}:
        res += x + y - l - dl
    else:
        res += abs(l - dl)

print(res)
