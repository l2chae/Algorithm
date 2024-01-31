# sys 모듈 말고 input 사용할 때 시간 초과

import sys

n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
l.sort()

def min(s):
    start = 0
    end = n-1
    while (start <= end):
        mid = (start + end) // 2
        if l[mid] < s:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1

def max(e):
    start = 0
    end = n-1
    while (start <= end):
        mid = (start + end) // 2
        if e < l[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end

for i in range(m):
    d1, d2 = map(int, sys.stdin.readline().split())
    print(max(d2) - min(d1) + 1)
