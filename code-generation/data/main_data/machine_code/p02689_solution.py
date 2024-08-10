def count_good_observatories(N, M, H, roads):
    good_obs = set()
    
    for i in range(1, N+1):
        is_good = True
        for road in roads:
            if i == road[0] or i == road[1]:
                if H[i-1] <= H[road[0]-1] or H[i-1] <= H[road[1]-1]:
                    is_good = False
                    break
        if is_good:
            good_obs.add(i)
    
    return len(good_obs)