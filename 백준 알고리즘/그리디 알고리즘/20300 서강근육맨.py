n = int(input())
arr = list(map(int, input().split()))
arr.sort()

if n % 2 == 0:
    res = arr[0] + arr[-1]
    N = n
else:
    res = arr[-1]
    N = n-1

for i in range(N//2):
    if res < arr[i] + arr[N-i-1]:
        res = arr[i] + arr[N-i-1]

print(res)
