#n분 일찍 일어난다고 하였을 때 알람시간 구하기
print('알람을 몇 분 일찍 맞출까요?')
N = int(input())
N_1 = N%60
N_2 = N//60

print('일어날 시간을 알려주세요.')
H, M= map(int, input().split())


if (N%60 <= M):
	print(H-N_2, M-N_1)
elif (0 <= M < N_1):
	if (0 < H <= 23):
		print(H-1-N_2, M+60-N_1)
	elif H == 0:
		print(H+23-N_2, M+60-N_1)
