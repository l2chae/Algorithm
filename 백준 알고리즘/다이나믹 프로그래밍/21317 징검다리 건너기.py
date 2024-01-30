n = int(input())
jump = [list(map(int, input().split())) for _ in range(n-1)]
k = int(input())

if n == 1:
    print(0)
    exit()
elif n == 2:
    print(jump[0][0])
    exit()

dp = [0] * n
dp[1] = jump[0][0]
dp[2] = min(dp[1] + jump[1][0], dp[0] + jump[0][1])

for i in range(3, n):
    dp[i] = min(dp[i-1] + jump[i-1][0], dp[i-2] + jump[i-2][1])

res = dp[-1]
dp2 = dp[:]  # dp2 = dp로 해서 틀렸는데, dp2 = dp는 복사가 아니라 그대로 할당이어서 dp2의 값이 변하면 dp값도 같이 변하므로 dp[:]로 복사본을 할당해야 함

for i in range(3, n):
    if dp[i-3] + k < dp[i]:
        dp2[i] = dp[i-3] + k
        for j in range(i+1, n):
            dp2[j] = min(dp[j], dp2[j-1] + jump[j-1][0], dp2[j-2] + jump[j-2][1])
        if dp2[-1] < res:
            res = dp2[-1]

print(res)
