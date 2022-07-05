def solution(id_list, report, k):
    l = len(id_list)
    answer = []
    rep = []
    count = [0 for _ in range(l)]
    arr = [[] for _ in range(l)]

    for i in report:
        rep.append(i.split())

    for i in rep:
        if i[1] not in arr[id_list.index(i[0])]:
            arr[id_list.index(i[0])].append(i[1])
            count[id_list.index(i[1])] += 1

    for i in arr:
        for j in range(l):
            if 0 < count[j] < k and id_list[j] in i:
                i.remove(id_list[j])

    for i in arr:
        answer.append(len(i))

    return answer
