#list 이용한 방법
lis = []
sum = 0

for i in range(int(input())):
    n = int(input())
    if n == 0:
        del lis[-1]
    else:
        lis.append(n)

for j in lis:
    sum += j

print(sum)


#stack 이용한 방법
stack = []

for i in range(int(input())):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))
