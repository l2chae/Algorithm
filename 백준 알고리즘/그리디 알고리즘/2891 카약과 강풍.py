# 문제에서 조건이 추가되었는데 못봐서 계속 틀림

n, s, r = map(int, input().split())
d = list(map(int, input().split()))
p = list(map(int, input().split()))

# 자신의 팀의 카약이 부서진 경우 먼저 제거
arr = []
for i in d:
    if i in p:
        p.remove(i)
    else:
        arr.append(i)

res = 0
for i in arr:
    if i-1 in p:
        p.remove(i-1)
    elif i+1 in p:
        p.remove(i+1)
    else:
        res += 1

print(res)
