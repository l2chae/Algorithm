import sys
from collections import deque

n, w, l = map(int, sys.stdin.readline().split())
a = deque(map(int, sys.stdin.readline().split()))

d = deque([0] * w)
count = 0
res = 0
while count < n:
    k = d.popleft()
    if k != 0:
        count += 1
    if len(a) > 0:
        if sum(d) + a[0] <= l:
            t = a.popleft()
            d.append(t)
        else:
            d.append(0)
    res += 1

print(res)
