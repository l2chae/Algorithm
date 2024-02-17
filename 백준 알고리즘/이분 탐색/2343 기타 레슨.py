import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

start = max(l)
end = sum(l)

res = sum(l)
while start <= end:
    mid = (start + end) // 2
    total = 0
    count = 1
    for i in l:
        if total + i <= mid:
            total += i
        else:
            count += 1
            total = i
    if count > m:
        start = mid + 1
    else:
        res = min(res, mid)
        end = mid - 1

print(res)
