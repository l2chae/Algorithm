def virus(graph, k, visited):
    visited[k] = True
    res.append(k)
    for i in graph[k]:
        if not visited[i]:
            virus(graph, i, visited)

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
for i in range(m):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)
    graph[num2].append(num1)

for i in range(n):
    graph[i+1].sort()

visited = [False] * (n+1)
res = []

virus(graph, 1, visited)
print(len(res)-1)
