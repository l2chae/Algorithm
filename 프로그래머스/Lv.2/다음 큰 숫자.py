def solution(n):
    cnt = format(n, 'b').count('1') # 4
    while True:
        n += 1 # 79, 80, ...
        if format(n, 'b').count('1') == cnt:
            answer = n
            break
        
    return answer
