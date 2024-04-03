import sys
from collections import deque
input = sys.stdin.readline

gear = [deque(map(int, input().strip())) for _ in range(4)]
k = int(input())
move = [list(map(int, input().split())) for _ in range(k)]

for i in range(k):
    stat = [0, 0, 0, 0]
    tmp = move[i][0] - 1
    stat[tmp] = move[i][1]
    while True:
        if tmp == 0:
            break
        if gear[tmp][-2] != gear[tmp-1][2]:
            if stat[tmp] == 1:
                stat[tmp-1] = -1
            elif stat[tmp] == -1:
                stat[tmp-1] = 1
        tmp -= 1
    tmp = move[i][0] - 1
    while True:
        if tmp == 3:
            break
        if gear[tmp][2] != gear[tmp+1][-2]:
            if stat[tmp] == 1:
                stat[tmp+1] = -1
            elif stat[tmp] == -1:
                stat[tmp+1] = 1
        tmp += 1
    for j in range(4):
        if stat[j] != 0:
            gear[j].rotate(stat[j])

res = 0
for i in range(4):
    if gear[i][0] == 1:
        res += 2 ** i

print(res)
