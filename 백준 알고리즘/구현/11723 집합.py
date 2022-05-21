import sys

m = int(sys.stdin.readline().rstrip())
s = []

for i in range(m):
    l = sys.stdin.readline().rstrip().split()
    if len(l) == 2: #숫자가 있을 때
        c, n = l[0], int(l[1])
        if c == 'add':
            if n not in s:
                s.append(n)
        elif c == 'remove':
            if n in s:
                s.remove(n)
        elif c == 'check':
            if n in s:
                print(1)
            else:
                print(0)
        elif c == 'toggle':
            if n in s:
                s.remove(n)
            else:
                s.append(n)
    else: #숫자가 없을 때
        c = l[0]
        if c == 'all':
            s = [i for i in range(1, 21)]
        elif c == 'empty':
            s = []
