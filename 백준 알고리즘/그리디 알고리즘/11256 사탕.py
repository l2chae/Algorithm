import sys
input = sys.stdin.readline

for i in range(int(input())):
    j, n = map(int, input().split())
    arr = []
    for i in range(n):
        r, c = map(int, input().split())
        arr.append(r*c)
    arr.sort(reverse=True)

    cnt = 0
    sum = 0
    for i in range(n):
        sum += arr[i]
        cnt += 1
        if sum >= j:
            break
    print(cnt)
