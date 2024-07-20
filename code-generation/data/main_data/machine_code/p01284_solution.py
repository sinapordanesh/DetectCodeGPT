def min_caffeine_needed(data):
    datasets = data.split('\n')
    results = []
    
    while datasets[0] != '0':
        T = int(datasets[0])
        sleep_hours = list(map(int, datasets[1].split()))
        N = int(datasets[2])
        interviews = []
        for i in range(3, 3+N):
            interviews.append(list(map(int, datasets[i].split())))
        
        caffeine = 0
        current_day = 1
        
        for interview in interviews:
            day_diff = interview[0] - current_day
            if day_diff < 0:
                day_diff += T
            caffeine += day_diff
            current_day = interview[0]
        
        results.append(caffeine)
        
        datasets = datasets[3 + N:]

    return results