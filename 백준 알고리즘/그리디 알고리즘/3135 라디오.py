a, b = map(int, input().split())
arr = [abs(a-b)]

for i in range(int(input())):
    n = int(input())
    arr.append(abs(n-b)+1)

print(min(arr))
