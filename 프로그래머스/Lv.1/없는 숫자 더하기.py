def solution(numbers):
    answer = 0
    num = [n for n in range(10)]
    for i in num:
        if i not in numbers:
            answer += i
    return answer
