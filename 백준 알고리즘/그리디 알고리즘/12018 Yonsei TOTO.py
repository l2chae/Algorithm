n, m = map(int, input().split())
res = []
for i in range(n):
    p, l = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    if p >= l:
        res.append(arr[l-1])
    else:
        res.append(1)
res.sort()

cnt = 0
for i in res: # 이부분에서 계속 틀렸음
    m -= i
    if m >= 0:
        cnt += 1

print(cnt)
