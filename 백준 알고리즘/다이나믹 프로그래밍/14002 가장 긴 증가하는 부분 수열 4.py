import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

res = []
k = max(dp)
for i in range(n-1, -1, -1):
    if dp[i] == k:
        if k == max(dp):
            res.append(arr[i])
        else:
            if arr[i] < res[-1]:
                res.append(arr[i])
        k -= 1

print(max(dp))
print(" ".join(map(str, res[::-1])))
