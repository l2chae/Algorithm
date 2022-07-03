# 프로그래머스 문제는 처음 풀어봤는데 input 값을 안받는지 몰라서 계속 틀렸다.

def solution(s):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        s = s.replace(arr[i], str(i))
    return int(s)
