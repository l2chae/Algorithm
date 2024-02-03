import sys

m, n = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

start = 1 # 과자 길이의 최솟값은 1이므로
end = max(l)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in l:
        total += x // mid
    if total < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)
