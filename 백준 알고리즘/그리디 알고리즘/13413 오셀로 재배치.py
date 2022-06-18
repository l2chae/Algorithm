t = int(input())
for i in range(t):
    n = int(input())
    arr1 = list(input())
    arr2 = list(input())
    cnt_w = 0
    cnt_b = 0
    for j in range(n):
        if arr1[j] != arr2[j]:
            if arr1[j] == 'W':
                cnt_w += 1
            else:
                cnt_b += 1
    if cnt_w == cnt_b:
        print(cnt_w)
    else:
        print(max(cnt_w, cnt_b))
