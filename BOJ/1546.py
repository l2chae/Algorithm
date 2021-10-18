N = int(input())
a = list(map(int, input().split()[:N]))
b=0

for i in range(len(a)):
    b+=(int(a[i])/max(a)*100) #b는 총합을 구한 것
print(b/N)
