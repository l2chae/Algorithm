n, m = map(int, input().split())
if n != 0:
    l = list(map(int, input().split()))

    cnt = 0
    tmp = 0
    for i in range(n):
        if tmp >= l[i]:
            tmp -= l[i]
        else:
            cnt += 1
            tmp = m-l[i]

    print(cnt)
else:
    print(0)
