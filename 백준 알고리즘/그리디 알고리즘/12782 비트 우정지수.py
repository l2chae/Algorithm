# 오셀로 재배치 문제와 같은 문제

for i in range(int(input())):
    n, m = input().split()
    cnt0 = 0
    cnt1 = 0
    for j in range(len(m)):
        if n[j] != m[j]:
            if n[j] == '0':
                cnt0 += 1
            else:
                cnt1 += 1
    if cnt0 == cnt1:
        print(cnt0)
    else:
        print(max(cnt0, cnt1))
