def chinese_classics(N, marks):
    order = []
    index = 0
    for i in range(N):
        if 'v' in marks[i]:
            continue
        elif marks[i] == '-':
            order.append(i+1)
        else:
            index += 1
            if int(marks[i][-1]) >= 2:
                continue
            elif int(marks[i][-1]) == 1:
                for j in range(i):
                    if marks[j] == marks[i][:-1]+'2':
                        order.insert(index-1, j+1)
    return order