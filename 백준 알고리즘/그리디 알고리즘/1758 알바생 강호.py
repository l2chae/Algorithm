n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)

res = 0
for i in range(n):
    if arr[i] >= i:
        res += arr[i] - i
print(res)
