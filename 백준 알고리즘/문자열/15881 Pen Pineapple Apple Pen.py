n = int(input())
s = input()

i = 0
cnt = 0

while i < n:
    if s[i:i+4] == 'pPAp':
        s = s[i+4:]
        cnt += 1
        i = 0
    else:
        i += 1

print(cnt)
