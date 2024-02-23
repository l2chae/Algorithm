import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

l = [arr[i+1] - arr[i] for i in range(n-1)]
l.sort()

print(sum(l[:n-k]))
