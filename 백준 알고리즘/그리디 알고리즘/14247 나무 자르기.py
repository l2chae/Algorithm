n = int(input())
h = list(map(int, input().split()))
a = list(map(int, input().split()))

tree = [[0] * 2 for _ in range(n)]
for i in range(n):
    tree[i][0], tree[i][1] = h[i], a[i]

tree.sort(key=lambda x:x[1])

res = 0
for i in range(n):
    res += tree[i][0] + (tree[i][1] * i)

print(res)
