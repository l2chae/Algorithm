import sys

n = int(sys.stdin.readline())
trees = list(map(int, sys.stdin.readline().split()))
flag = sum(trees) // 3

count = 0
if sum(trees) % 3 == 0:
    for tree in trees:
        count += tree // 2
    if count >= flag:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
