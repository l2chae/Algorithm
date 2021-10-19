#머리로는 이해가 되지만 구현이 조금 어려웠다.
a = []
for i in range(10):
    a.append(int(input())%42)
a_set = set(a)
print(len(a_set))


#더 간단하게 작성할 수 있는 방안을 찾아본 것
#여러줄에 걸쳐 입력하는 방법
a = [int(input())%10 for i in range(10)]
print(len(set(a)))
