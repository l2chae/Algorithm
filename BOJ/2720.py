t = int(input())
coin = [25, 10, 5, 1] #쿼터 0.25, 다임 0.10, 니켈 0.05, 페니 0.01

for i in range(t):
    n = int(input())
    cnt = []
    for j in range(4):
        cnt.append(n // coin[j])
        n %= coin[j]
    print(*cnt) #*는 리스트 언패킹
