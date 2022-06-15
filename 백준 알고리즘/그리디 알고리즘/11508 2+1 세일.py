n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)

res = 0
for i in range(n):
    if i % 3 != 2:
        res += arr[i]
print(res)
