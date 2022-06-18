for i in range(int(input())):
    n = int(input())
    arr = list(input().split())
    lft = arr[0]
    res = arr[0]
    for i in range(1, n):
        if lft < arr[i]:
            res += arr[i]
        else:
            res = arr[i] + res
            lft = arr[i]
    print(res)
