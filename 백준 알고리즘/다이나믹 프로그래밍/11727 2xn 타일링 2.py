# 규칙을 못찾아서 한참 헤맸던 문제

n = int(input())

dp = [0 for i in range(n+2)]
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = dp[i-2] * 2 + dp[i-1]
    dp[i] %= 10007

print(dp[n])
