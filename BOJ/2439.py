N = int(input())

for i in range(N):
    print(('*' * (i+1)).rjust(N))
    #오른쪽 정렬은 .rjust()로, 왼쪽 정렬은 .ljust()로
