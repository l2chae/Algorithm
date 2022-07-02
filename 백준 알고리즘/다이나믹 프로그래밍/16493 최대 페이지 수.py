# 퇴사 문제랑 비슷한 문제..?

n, m = map(int, input().split())
arr = [[] for _ in range(m+1)]
for i in range(1, m+1):
    arr[i] = list(map(int, input().split()))

dp = [[0 for j in range(n+1)] for j in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        if j - arr[i][0] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i][0]] + arr[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])
