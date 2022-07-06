# 규칙을 2차원 배열로 찾으려 했음.

n = int(input())

dp = [0] * (n+1)

for i in range(n+1):
    if i == 1:
        dp[i] = 3
    elif i == 2:
        dp[i] = 7
    else:
        dp[i] = dp[i-1] * 2 + dp[i-2]
        dp[i] %= 9901

print(dp[n])
