n = int(input())

if (1 <= n <= 9):
	for k in range(1, 10):
		print('{} * {} = {}'.format(n, k, n*k))
    #파이썬 format에는 여러가지가 있다는 것을 알게됨
    #print(f'{n} * {k} = {n*k}') 이렇게 더 간결하게 쓸 수 있음
else:
	print('Error')
