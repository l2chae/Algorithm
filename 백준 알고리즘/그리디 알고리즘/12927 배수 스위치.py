# 출력에 모든 스위치가 꺼지지 않는다면 -1 출력인데 안해도 맞는다..?

s = list(input())

cnt = 0
for i in range(len(s)):
    if s[i] == 'Y':
        for j in range(i, len(s), i+1):
            if s[j] == 'Y':
                s[j] = 'N'
            else:
                s[j] = 'Y'
        cnt += 1

print(cnt)
