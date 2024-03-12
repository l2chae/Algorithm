import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[1] * (n+1) for _ in range(k)]

for i in range(1, k):
    for j in range(1, n+1):
        dp[i][j] = sum(dp[i-1][:j+1])

print(dp[-1][-1] % 1000000000)
