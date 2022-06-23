# 계속 시간 초과가 났는데, 테스트 케이스 for문 안에 dp 구현이 문제였다.

import sys
input = sys.stdin.readline

dp = [1] * (1000001)
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    dp[i] %= 1000000009
    
for i in range(int(input())):
    n = int(input())
    print(dp[n])
