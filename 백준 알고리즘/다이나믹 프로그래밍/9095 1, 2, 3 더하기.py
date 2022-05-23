'''
규칙 찾는 것이 어려웠던 문제
i>=4 일때, i-3인 경우에는 3을, i-2인 경우에는 2를, i-1인 경우에는 1을 더하면 i가 가진 경우의 수를 만들 수 있음
'''

def sum(n):
    dp = [0] * (n+3)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    
    return(dp[n])

for i in range(int(input())):
    n = int(input())
    print(sum(n))
