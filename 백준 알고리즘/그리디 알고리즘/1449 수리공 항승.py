# 그리디 문제를 중점적으로 연습해야겠다는 생각이 들었음.

n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0
start = arr[0]
end = start + l
for i in range(n):
    if arr[i] < end:
        continue
    else:
        cnt += 1
        end = arr[i] + l

print(cnt+1)
