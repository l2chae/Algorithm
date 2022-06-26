n = int(input())
arr = list(map(int, input().split()))
jw = arr[0]
arr = arr[1:]
arr.sort()

flag = 1 # n이 1일때는 Yes이므로 flag값을 1로 설정해주어야 함
for i in range(n-1):
    if jw > arr[i]:
        jw += arr[i]
        arr[i] = 0
        flag = 1
    else:
        flag = 0

if flag:
    print('Yes')
else:
    print('No')
