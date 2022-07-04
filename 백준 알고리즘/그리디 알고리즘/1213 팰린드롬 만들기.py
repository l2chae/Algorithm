# 생각보다 코드가 안깔끔해서 고쳐야 할듯...

s = list(input())
arr = [0] * 26
cnt = 0
for i in range(65, 91):
    arr[i-65] = s.count(chr(i))
    if s.count(chr(i)) % 2 != 0:
        cnt += 1

res = ''
k = ''
if cnt > 1:
    print("I'm Sorry Hansoo")
else:
    for i in range(26):
        if arr[i] != 0:
            res += chr(i+65) * (arr[i]//2)
        if arr[i] % 2 != 0:
            k = chr(i+65)
    print(res + k + res[::-1])
