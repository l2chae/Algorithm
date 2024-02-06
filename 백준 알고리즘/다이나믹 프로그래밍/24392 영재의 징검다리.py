import sys

n, m = map(int, sys.stdin.readline().split())
l = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]
dp[n-1] = l[n-1]

for i in range(n-2, -1, -1):
    for j in range(m):
        if l[i][j] == 1:
            if j == 0:
                dp[i][j] += dp[i+1][j] + dp[i+1][j+1]
            elif j == m-1:
                dp[i][j] += dp[i+1][j-1] + dp[i+1][j]
            else:
                dp[i][j] += dp[i+1][j-1] + dp[i+1][j] + dp[i+1][j+1]

print(sum(dp[0]) % 1000000007)
