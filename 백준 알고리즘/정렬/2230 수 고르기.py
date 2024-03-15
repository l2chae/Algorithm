import sys

n, m = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()

end = 1
res = 2000000000
for i in range(n):
    while arr[end] - arr[i] < m and end < n-1:
        end += 1
    if arr[end] - arr[i] >= m:
        res = min(res, arr[end] - arr[i])

print(res)
