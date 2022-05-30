'''
for문을 많이 써서 시간초과가 남
서류 등수로 정렬한 뒤 비교하면 됐던 문제
'''

import sys
input = sys.stdin.readline

for i in range(int(input())):
    n = int(input())

    arr_rank = []
    for j in range(n):
        arr_rank.append(list(map(int, input().split())))
    arr_rank.sort()
    
    arr_res = [1] * n
    s = arr_rank[0][1]
    for j in range(1, n):
        if s > arr_rank[j][1]:
            s = arr_rank[j][1]
        else:
            arr_res[j] = 0
    
    print(arr_res.count(1))
