# 그리디 풀이
n = int(input())
cnt = 0

while n > 0:
    if n % 5 == 0:
        n -= 5
        cnt += 1
    elif n % 2 == 0:
        n -= 2
        cnt += 1
    elif n > 5:
        n -= 5
        cnt += 1
    else:
        cnt = -1
        break

print(cnt)


# dp 이용 풀이
n = int(input())

def change(n):
    dp = [100001] * (n+5)
    dp[2] = 1
    dp[4] = 2
    dp[5] = 1
    for i in range(6, n+1):
        dp[i] = min(dp[i-2], dp[i-5]) + 1
    return dp[n]

if change(n) != 100001:
    print(change(n))
else:
    print(-1)
