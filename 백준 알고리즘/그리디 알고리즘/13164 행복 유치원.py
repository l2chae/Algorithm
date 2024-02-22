import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

l = []
for i in range(n-1):
    l.append(arr[i+1] - arr[i])

l.sort()
print(sum(l[:n-k]))
