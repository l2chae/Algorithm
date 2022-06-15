n = int(input())
arr = [0]
for i in range(n):
    s, e, p = map(int, input().split())
    arr.append(p)

dp = [0] * (n+1)
dp[1] = arr[1]
for i in range(2, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + arr[i])

print(dp[-1])
