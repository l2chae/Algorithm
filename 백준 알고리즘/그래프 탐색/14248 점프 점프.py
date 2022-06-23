def dfs(x):
    visited[x] = True
    for i in range(2):
        if i == 0:
            nx = x + arr[x]
        else:
            nx = x - arr[x]
        if nx < 0 or nx >= n:
            continue
        if not visited[nx]:
            dfs(nx)

n = int(input())
arr = list(map(int, input().split()))
s = int(input())

visited = [False] * n

dfs(s-1)

print(visited.count(True))
