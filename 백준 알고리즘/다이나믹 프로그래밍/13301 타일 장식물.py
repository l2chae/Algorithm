n = int(input())

def tile(n):
    dp = [0] * (n+2)
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return 2 * (dp[n] + 2 * dp[n-1] + dp[n-2])

print(tile(n))
