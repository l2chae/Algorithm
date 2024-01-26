N = int(input())
list_N = set(map(int, input().split()))
M = int(input())
list_M = list(map(int, input().split()))

for i in range(M):
    if list_M[i] in list_N:   # set(집합 자료형)에서의 포함 여부 확인은 O(1)의 시간 복잡도
        print(1)
    else:
        print(0)
