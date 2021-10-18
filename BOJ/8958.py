#합을 구하는 것에서 막혔던 문제
#하지만 각 O의 카운트 횟수가 점수이므로 카운트 값을 더하면 됐던 것
t = int(input())

for i in range(t):
    n = list(input())    
    c = 0
    s = 0
    for j in range(len(n)):
        if (n[j]=='O'):
            c += 1
            s += c
        else :
            c = 0
            continue
    print(s)
