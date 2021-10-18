a = int(input())
b = int(input())
c = int(input())
abc = str(a*b*c)

for i in range(10):
    count = abc.count(f'{i}') #format을 사용한 이유는 str을 인식해야하기 때문
    print(count)
