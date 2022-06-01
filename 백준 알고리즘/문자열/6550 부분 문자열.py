while True:
    try:
        s, t = input().split()
        s = list(s)
        t = list(t)

        arr = []
        for i in range(len(s)):
            if s[i] in t:
                arr.append(s[i])
                t = t[t.index(s[i])+1:]
        
        if arr == s:
            print('Yes')
        else:
            print('No')
    except:
        break
