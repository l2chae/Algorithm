# 확률을 생각해야하는 dp문제

n = int(input())

# 1이 상근, 0이 창영
dp = [0] * (n+4)
dp[1] = 1
dp[3] = 1
dp[4] = 1

for i in range(5, n+1):
    if dp[i-1] + dp[i-3] + dp[i-4] < 3: # 모두 상근이가 이기는 경우에는 무조건 창영이가 이기기 때문
        dp[i] = 1
    else:
        dp[i] = 0

if dp[n] == 1:
    print('SK')
else:
    print('CY')
