def schedule_matches(N, matches):
    days = 1
    while True:
        flag = True
        played = set()
        for i in range(N):
            if i+1 in played:
                flag = False
                break
            for j in range(N-1):
                if matches[i][j] in played:
                    flag = False
                    break
                played.add(i+1)
                played.add(matches[i][j])
        if flag:
            return days
        days += 1
        if days > N:
            return -1