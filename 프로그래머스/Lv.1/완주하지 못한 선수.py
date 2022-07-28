def solution(participant, completion):
    dic = {i: 0 for i in participant}

    for i in participant:
        dic[i] += 1

    for i in completion:
        dic[i] -= 1

    for k, v in dic.items():
        if v != 0:
            answer = k

    return answer
