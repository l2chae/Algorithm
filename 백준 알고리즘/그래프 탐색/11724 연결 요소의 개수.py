import sys
sys.setrecursionlimit(10**6) # 런타임 에러(recursion error)가 나서 추가
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    arr[u-1].append(v)
    arr[v-1].append(u)

visited = [False] * n

def link(s):
    visited[s] = True
    for i in arr[s]:
        if not visited[i-1]:
            link(i-1) # i 라 해서 계속 오류 났던 부분

cnt = 0
for i in range(n):
    if not visited[i]:
        link(i)
        cnt += 1
print(cnt)
