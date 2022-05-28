n = int(input())
lis = list(map(int, input().split()))
arr = [[1 for j in range(n)] for i in range(2)] # arr[0] 증가, arr[1] 감소 저장

for i in range(1, n):
    if lis[i-1] <= lis[i]:
        arr[0][i] = arr[0][i-1] + 1
    if lis[i-1] >= lis[i]:
        arr[1][i] = arr[1][i-1] + 1

print(max(max(arr[0]), max(arr[1])))
