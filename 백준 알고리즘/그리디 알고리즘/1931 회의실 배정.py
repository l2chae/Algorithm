'''
1946번 문제와 비슷
다른 점은 끝나는 시간(두번째 인덱스)를 기준으로 정렬 해야 한다는 것
'''

import sys
input = sys.stdin.readline

n = int(input())

time = []
for i in range(n):
    time.append(list(map(int, input().split())))
time.sort(key=lambda x: (x[1], x[0])) # 인덱스 1을 기준으로 오름차순, 같은 값에 대해서는 인덱스 0을 기준으로 
    
cnt = 1
s = time[0][1]
for i in range(1, n):
    if s <= time[i][0]:
        s = time[i][1]
        cnt += 1

print(cnt)
