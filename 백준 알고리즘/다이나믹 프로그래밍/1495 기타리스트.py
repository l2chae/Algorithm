n, s, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0 for j in range(n+1)] for i in range(m+1)]
dp[s][0] = 1

for j in range(n):
    for i in range(m+1):
        if dp[i][j] != 0:
            if i - arr[j] > -1:
                dp[i-arr[j]][j+1] = 1
            if i + arr[j] < m+1:
                dp[i+arr[j]][j+1] = 1

res = -1
for i in range(m+1):
    if dp[i][-1] != 0:
        res = i
print(res)
