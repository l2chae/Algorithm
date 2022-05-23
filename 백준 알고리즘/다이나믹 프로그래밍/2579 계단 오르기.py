'''
-OXO, -OXOO 인 경우를 생각하면 간단한 문제
점화식 구현이 잘 안됐었음
'''

def stairs(n):
    dp = [0] * (n+3)
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]
    dp[3] = max(dp[1]+arr[3], arr[2]+arr[3])
    for i in range(4, n+1):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i])
    return dp[n]

n = int(input())
arr = [0] * (n+3) # 1, 2, 3일 때 런타임 에러가 자주 나는 부분
for i in range(n):
    p = int(input())
    arr[i+1] = p

print(stairs(n))
