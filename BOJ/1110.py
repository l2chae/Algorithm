#자릿수를 생각해서 계산한 것 좀더 간단하게 작성할 필요가 있었다
num = str(input().zfill(2))
sum = str(int(num[0]) + int(num[1])).zfill(2)
add = num[1] + sum[1]
i = 1

while(num!=add):
    sum = str(int(add[0]) + int(add[1])).zfill(2)
    add = add[1] + sum[1]
    i += 1
print(i)
