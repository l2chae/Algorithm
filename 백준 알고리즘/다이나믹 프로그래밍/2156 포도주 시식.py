'''
계단 오르기와 비슷한 문제
마지막을 꼭 선택할 필요가 없다는 것이 다른 부분
'''

def stairs(n):
    dp = [0] * (n+3)
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]
    dp[3] = max(dp[1]+arr[3], arr[2]+arr[3], dp[2]) # 마지막 잔을 고를 필요가 없기 때문에 dp[2] 추가
    for i in range(4, n+1):
        dp[i] = max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i], dp[i-1])
    return dp[n]

n = int(input())
arr = [0] * (n+3)
for i in range(n):
    p = int(input())
    arr[i+1] = p

print(stairs(n))
