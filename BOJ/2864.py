a, b = input().split()
mini = maxi = length = ''

if len(a) >= len(b):
    length = len(a)
else:
    length = len(b)

#min
for i in range(length):
    if a[i] == '6':
        a = a.replace('6', '5')
    if b[i] == '6':
        b = b.replace('6', '5')
    mini = int(a)+int(b)

#max
for i in range(length):
    if a[i] == '5':
        a = a.replace('5', '6')
    if b[i] == '5':
        b = b.replace('5', '6')
    maxi = int(a)+int(b)

print(mini, maxi)
