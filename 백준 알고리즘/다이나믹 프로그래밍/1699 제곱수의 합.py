n = int(input())
INF = 100001

dp = [INF] * (n+1)
dp[0] = 0


for i in range(1, n+1):
    for j in range(1, int(i**(1/2))+1):
        if dp[i] > dp[i - j*j]: # j**2로 하면 시간 초과 발생
            dp[i] = dp[i - j*j] + 1

print(dp[n])
