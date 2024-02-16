import sys

n = int(sys.stdin.readline())
l = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
l.sort(key=lambda x:(x[0], x[1]))

start = l[0][0]
end = l[0][1]
res = end - start
for i in range(1, n):
    if l[i][0] < end < l[i][1]:
        start = end
        end = l[i][1]
        res += (end - start)
    if start <= l[i][0] and end <= l[i][1]:
        start = end
    if end <= l[i][0]:
        start = l[i][0]
        end = l[i][1]
        res += (end - start)

print(res)
