import sys

n, k = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]

start = 1
end = sum(arr) + k
res = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in arr:
        if x < mid:
            total += mid - x
    if total > k:
        end = mid - 1
    else:
        res = max(res, mid)
        start = mid + 1

print(res)
