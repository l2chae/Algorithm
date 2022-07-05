# 규칙 찾기 힘들었던 문제

n = int(input())
arr = [[1 for j in range(10)] for i in range(n)]

for i in range(1, n):
    for j in range(10):
        if j == 0:
            arr[i][j] = sum(arr[i-1])
            arr[i][j] %= 10007
        else:
            arr[i][j] = arr[i][j-1] - arr[i-1][j-1]
            arr[i][j] %= 10007

print(sum(arr[-1]) % 10007)
