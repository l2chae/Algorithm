n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for i in range(m):
    s = arr[0] + arr[1]
    arr[0] = s
    arr[1] = s
    arr.sort()
    
print(sum(arr))
