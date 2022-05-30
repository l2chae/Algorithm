import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    r = int(input())
    arr.append(r)
arr.sort()

cnt = 0
for i in range(n):
    if arr[i] != i+1:
        cnt += abs(arr[i] - (i+1))

print(cnt)
