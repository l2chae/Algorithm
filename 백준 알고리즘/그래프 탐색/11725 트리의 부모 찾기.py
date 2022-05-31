import sys
sys.setrecursionlimit(10 ** 6) # 재귀 깊이 설정해주는 것 잊지 말것
input = sys.stdin.readline

def dfs(v):
    for i in arr[v]:
        if res[i] == 0:
            res[i] = v
            dfs(i)

n = int(input())
arr = [[] for i in range(n+1)]
for i in range(n-1):
    n1, n2 = map(int, input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

for i in range(n):
    arr[i+1].sort()

res = [0 for i in range(n+1)]
res[1] = 1

dfs(1)
res = res[2:]

for i in res:
    print(i)
