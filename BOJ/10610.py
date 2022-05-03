n = input()
lis = list(map(int, n))
lis.sort(reverse=True)

if (sum(lis) % 3 == 0) and (0 in lis):
    for i in lis:
        print(i, end='')
else:
    print(-1)
