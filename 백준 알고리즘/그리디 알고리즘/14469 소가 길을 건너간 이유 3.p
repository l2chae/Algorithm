n = int(input())
arr = [[0 for j in range(2)] for i in range(n)]
for i in range(n):
    a, c = map(int, input().split())
    arr[i][0] = a
    arr[i][1] = c
arr.sort(key=lambda x : x[0])

res = 0
for i in range(n):
    if res <= arr[i][0]:
        res = sum(arr[i])
    else:
        res += arr[i][1]
print(res)
