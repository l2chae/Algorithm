arr = []
for i in range(int(input())):
    arr.append(input())

arr = list(set(arr))
arr.sort()
arr.sort(key=lambda x: len(x))

print('\n'.join(arr))
