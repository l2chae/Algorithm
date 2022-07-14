w = input()
arr = [w[i:] for i in range(len(w))]
arr.sort()
print('\n'.join(arr))
