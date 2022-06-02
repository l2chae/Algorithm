n = int(input())
c = int(input())
v = [int(input()) for i in range(n-1)]
v.sort(reverse=True)

cnt = 0
if n == 1:
    print(0)
else:
    while v[0] >= c:
        c += 1
        v[0] -= 1
        cnt += 1
        v.sort(reverse=True)
    print(cnt)
