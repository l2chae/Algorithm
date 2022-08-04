# 백준에서 비슷한 문제를 풀었던 기억이 있어서 쉽게 풀었지만 정렬을 해야 됐던 문제

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    arr = []
    for i in lost:
        if i in reserve:
            reserve.remove(i)
        else:
            arr.append(i)

    for i in arr:
        if i-1 in reserve:
            reserve.remove(i-1)
        elif i+1 in reserve:
            reserve.remove(i+1)
        else:
            n -= 1
    return n
