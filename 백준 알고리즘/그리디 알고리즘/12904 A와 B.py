import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

while len(t) > len(s):
    if t[-1] == "A":
        t = t[:-1]
    else:
        t = t[:-1][::-1]

if t == s:
    print(1)
else:
    print(0)
