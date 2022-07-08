def solution(numbers, hand):
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2], '*': [3, 0], 0: [3, 1], '#': [3, 2]}
    lh = '*'
    rh = '#'
    answer = ''
    for i in numbers:
        if dic[i][1] == 0:
            answer += 'L'
            lh = i
        elif dic[i][1] == 2:
            answer += 'R'
            rh = i
        else:
            dis_l = abs(dic[lh][0]-dic[i][0]) + abs(dic[lh][1]-dic[i][1])
            dis_r = abs(dic[rh][0]-dic[i][0]) + abs(dic[rh][1]-dic[i][1])
            if dis_l < dis_r:
                answer += 'L'
                lh = i
            elif dis_l > dis_r:
                answer += 'R'
                rh = i
            else:
                if hand == "left":
                    answer += 'L'
                    lh = i
                else:
                    answer += 'R'
                    rh = i
    return answer
