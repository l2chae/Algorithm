# 규칙 찾기 힘들었던 문제

t = int(input())

dp = [0] * (10001)

for i in range(1, 10001):
    if i < 4:
        dp[i] = i
    else:
        dp[i] = dp[i-3] + i//2 + 1

for i in range(t):
    n = int(input())
    print(dp[n])
