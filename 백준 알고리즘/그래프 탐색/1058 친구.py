# for문을 이용해 풀었음

def f(v, c):
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            visited[i] = True
            for j in arr[i]:
                if not visited[j] and j not in arr[v]:
                    visited[j] = True
                    c += 1
    res[v] = c
            

n = int(input())
arr = [[] for _ in range(n)]
for i in range(n):
    s = list(input())
    for j in range(n):
        if s[j] == 'Y':
            arr[i].append(j)

res = [0] * n
for i in range(n):
    visited = [False] * n
    f(i, len(arr[i]))

print(max(res))
