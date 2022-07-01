# 이항계수 문제

n = int(input())
m = int(input())

dp = [[0 for j in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):
        if j == 0 or i == j:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[-1][-1])
