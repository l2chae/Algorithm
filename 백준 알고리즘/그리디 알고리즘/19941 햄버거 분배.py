# 범위를 앞, 뒤 나눠서 안해도 됐었음

n, k = map(int, input().split())
arr = list(input())

cnt = 0
for i in range(n):
    if arr[i] == 'P':
        for j in range(max(i-k, 0), min(i+k+1, n)):
            if arr[j] == 'H':
                arr[j] = 'X'
                cnt += 1
                break

print(cnt)
