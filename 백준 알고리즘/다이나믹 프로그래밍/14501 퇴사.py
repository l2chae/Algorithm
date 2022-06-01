'''
뒤에서 풀어야 했던 문제는 처음이라 어려웠음
dfs/bfs로도 풀 수 있는 문제(기회가 되면 풀어봐야겠다)
'''
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [0 for j in range(n+5)]
for i in range(n-1, -1, -1):
    if i + arr[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], arr[i][1] + dp[i + arr[i][0]])
print(dp[0])
