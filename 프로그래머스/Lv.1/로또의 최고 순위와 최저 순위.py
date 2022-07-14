def solution(lottos, win_nums):
    answer = [0] * 2
    dic = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    corr = 0
    for i in lottos:
        if i in win_nums:
            corr += 1
    zero = lottos.count(0)
    answer[0] = dic[corr+zero]
    answer[1] = dic[corr]
    return answer
