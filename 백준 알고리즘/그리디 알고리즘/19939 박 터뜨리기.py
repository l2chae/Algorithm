# 규칙을 찾으면 쉬운 문제

n, k = map(int, input().split())

sum = 0
for i in range(1, k+1):
    sum += i

if n < sum:
    print(-1)
else:
    if k % 2 == 0:
        if n % k == k//2:
            print(k-1)
        else:
            print(k)
    else:
        if n % k == 0:
            print(k-1)
        else:
            print(k)
