import sys

n = int(sys.stdin.readline())
ab = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    ab.append([a, b])
ab.sort(key=lambda x: (x[0], x[1]))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if ab[j][1] < ab[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))
