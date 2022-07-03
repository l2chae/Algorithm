# 처음 풀어보는 프로그래머스 문제. 입력값 안받는지 몰라서 계속 헤맸음.

def solution(s):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        s = s.replace(arr[i], str(i))
    return int(s)
