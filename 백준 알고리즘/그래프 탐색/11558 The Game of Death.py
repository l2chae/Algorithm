'''
답은 잘 나오는데 계속 틀렸다고 해서 애먹은 문제(아직도 왜 틀렸는지 모르겠다)
'''

import sys
sys.setrecursionlimit(10 ** 6)

def the_game_of_death(v):
    for i in arr[v]:
        if visited[i] == 0:
            visited[i] = visited[v] + 1
            the_game_of_death(i)

for i in range(int(input())):
    n = int(input())
    arr = [[] for i in range(n+1)]
    for j in range(n):
        arr[j+1].append(int(input()))
    '''
    arr = [[]]
    for j in range(n):
        arr.append(list(map(int, input())))
    이렇게 했을 때는 틀렸는데 뭐가 다른건지 잘 모르겠다
    '''

    visited = [0] * (n+1)

    the_game_of_death(1)
    print(visited[n])
