import sys
input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(n+2)]
for i in range(1, n+1):
    s, e, p = map(int, input().split())
    arr[i] = p

dp = [0] * (n+1)
dp[1] = arr[1]
for i in range(2, n+1):
    if i == 2:
        dp[i] = max(dp[i-1], arr[i])
    else:
        dp[i] = max(dp[i-2] + arr[i], dp[i-1])

print(dp[-1])
