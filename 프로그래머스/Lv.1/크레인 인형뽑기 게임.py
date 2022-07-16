def solution(board, moves):
    answer = 0
    stack = [0]
    for i in moves:
        for j in board:
            if j[i-1] != 0:
                if j[i-1] != stack[-1]:
                    stack.append(j[i-1])
                    j[i-1] = 0
                    break
                else:
                    stack.pop()
                    j[i-1] = 0
                    answer += 1
                    break
    return answer*2
