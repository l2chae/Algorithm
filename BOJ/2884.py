#시를 기준으로 나눈 것
H, M = map(int, input().split())

if (0 < H <= 23):
	if (45 <= M <= 59):
		print(H, M-45)
	elif (0 <= M < 45):
		print(H-1, M+15)
elif H == 0:
	if (45 <= M <= 59):
		print(H, M-45)
	elif (0 <= M < 45):
		print(H+23, M+15)
    

#분을 기준으로 나눈 것
H, M = map(int, input().split())

if (45 <= M <= 59):
		print(H, M-45)
elif (0 <= M < 45):
	if (0 < H <= 23):
		print(H-1, M+15)
	elif H == 0:
		print(H+23, M+15)
