import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

start = 0
end = max(l)

res = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in l:
        if i <= mid:
            total += i
        else:
            total += mid
    if total > m:
        end = mid - 1
    else:
        res = max(res, mid)
        start = mid + 1

print(res)
