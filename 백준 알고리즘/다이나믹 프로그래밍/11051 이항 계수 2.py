n, k = map(int, input().split())

def binomial2(n, k):
    dp = [[0 for j in range(n+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(n+1):
            if j == 0 or j == i:
                dp[i][j] = 1
            if 0 < j < i:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            dp[i][j] %= 10007
    
    return dp[n][k]

print(binomial2(n, k))
