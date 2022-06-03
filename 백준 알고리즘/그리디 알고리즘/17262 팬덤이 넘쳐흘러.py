# 가장 늦게 등교한 학생의 시간 - 가장 일찍 하교한 학생의 시간만큼을 제외해주면 됐던 문제

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

s = sorted(arr, key=lambda x: x[0])
e = sorted(arr, key=lambda x: x[1])
res = s[-1][0] - e[0][1]

if res <= 0:
    print(0)
else:
    print(res)
