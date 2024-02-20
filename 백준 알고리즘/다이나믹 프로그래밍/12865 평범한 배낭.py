import sys

n, k = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0] * (n+1) for _ in range(k+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if arr[i-1][0] <= j:
            dp[j][i] = max(dp[j][i-1], arr[i-1][1] + dp[j-arr[i-1][0]][i-1])
        else:
            dp[j][i] = dp[j][i-1]

print(dp[-1][-1])
