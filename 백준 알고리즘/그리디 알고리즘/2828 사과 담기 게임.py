n, m = map(int, input().split())
j = int(input())
p = [int(input()) for i in range(j)]

s = 1 # 처음 시작 위치는 1번칸부터 m번칸까지 담을 수 있는 위치
f = m
cnt = 0
for i in range(j):
    if f < p[i]:
        cnt += p[i] - f
        s = p[i] - (m-1)
        f = p[i]
    elif s > p[i]:
        cnt += s - p[i]
        s = p[i]
        f = p[i] + (m-1)

print(cnt)
