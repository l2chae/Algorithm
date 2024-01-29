n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]

res = 0
for i in land:
    res += sum(i)

time = 0
max_height= (res+b)//(n*m)
block = b
dic = {} # time: height
for i in range(max_height, -1, -1):
    for j in land:
        for k in j:
            if k < i:  # 채워넣기
                block -= (i-k)
                time += (1*(i-k))
            elif k > i:  # 깎기
                block += (k-i)
                time += (2*(k-i))

    if block >= 0:
        if not dic:
            dic[time] = i
        else:
            if time < next(iter(dic)):
                if time in dic:
                    if i > dic[time]:
                        dic[time] = i
                else:
                    dic[time] = i
    else:
        break
    time = 0
    block = b

dic = sorted(dic.items())
print(dic[0][0], dic[0][1])
