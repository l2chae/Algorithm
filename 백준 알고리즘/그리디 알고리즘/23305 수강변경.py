n = int(input())

data = [0] * 1000001

for i in list(map(int, input().split())) :
  data[i] += 1

res = 0
for i in list(map(int, input().split())):
    if data[i] > 0:
        data[i] -= 1
    else:
        res += 1
print(res)
