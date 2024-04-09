import sys
input = sys.stdin.readline

h, w = map(int, input().split())
block = list(map(int, input().split()))

res = 0
for i in range(1, w-1):
    height = min(max(block[:i]), max(block[i+1:]))
    if height >= block[i]:
        res += height - block[i]

print(res)
