'''
2차원 배열을 통해서 풀었는데 팩토리얼을 이용해서 풀 수도 있는 문제였다
'''

def bridge(x, y):
    dp = [[0 for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            if i > j:
                continue
            if i == 0:
                dp[i][j] = j+1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    return dp[x][y]

for i in range(int(input())):
    n, m = map(int, input().split())
    print(bridge(n-1, m-1))
