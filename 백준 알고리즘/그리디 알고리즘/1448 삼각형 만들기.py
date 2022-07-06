import sys
input = sys.stdin.readline # 시간 초과의 원인

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)

res = -1
for i in range(n-2):
    if arr[i] < arr[i+1] + arr[i+2]:
        res = sum(arr[i:i+3])
        break

print(res)
