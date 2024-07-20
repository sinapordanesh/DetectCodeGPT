def stopped_watches(datasets):
    results = []
    for data in datasets:
        watches = data.split("\n")
        if watches[0] == '0':
            break
        times = []
        for i in range(1, len(watches)):
            s, t, u = map(int, watches[i].split())
            times.append((s, t, u))
        
        candidates = set()
        for h in range(12):
            for m in range(60):
                for s in range(60):
                    valid = True
                    for time in times:
                        s_i = (time[0] + 12 * h) % 60
                        t_i = (time[1] + 5 * m) % 60
                        u_i = (time[2] + m) % 60
                        if s_i != s and t_i != s and u_i != s:
                            valid = False
                            break
                    if valid:
                        candidates.add((h, m, s))
        
        sorted_candidates = sorted(list(candidates))
        results.append("{:02d}:{:02d}:{:02d} {:02d}:{:02d}:{:02d}".format(sorted_candidates[0][0], sorted_candidates[0][1], sorted_candidates[0][2], sorted_candidates[-1][0], sorted_candidates[-1][1], sorted_candidates[-1][2]))
    
    return results