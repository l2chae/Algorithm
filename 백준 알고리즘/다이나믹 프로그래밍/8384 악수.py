import sys

n = int(input())
dp = [0] * (n+2)
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1]%10 + dp[i-2]%10)%10 # 원래는 int(str(dp[i-1] + dp[i-2])[-1]) 이렇게 했었는데 시간초과가 발생함

print(dp[n])
