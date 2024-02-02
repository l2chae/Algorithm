import sys

n = int(sys.stdin.readline())

t = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    t.append(-(a-b))
t.sort()

mid = (n-1) // 2
if n % 2 == 0:
    print(abs(t[mid+1] - t[mid]) + 1)
else:
    print(1)
