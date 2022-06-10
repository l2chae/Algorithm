def dfs(v, c):
    visited[v] = True
    if c == 2:
        return 0
    for i in arr[v]:
        # if not visited[i] 때문에 틀렸음
        dfs(i, c+1)

n = int(input())
arr = [[] for _ in range(n+1)]
for i in range(int(input())):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (n+1)

dfs(1, 0)
print(visited.count(True)-1)
