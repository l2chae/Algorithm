n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for j in range(m)] for i in range(n)]
dp[0][0] = arr[0][0]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0: # 이부분이 없어서 1 1 배열일때 값이 두배가 됨
            continue
        if i == 0:
            dp[i][j] = dp[i][j-1] + arr[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + arr[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + arr[i][j]

print(dp[-1][-1])
