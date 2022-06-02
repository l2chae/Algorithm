import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(1, n):
    arr[i] = max(arr[i], arr[i]+arr[i-1])
   
print(max(arr))
