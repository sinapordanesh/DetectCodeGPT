def donut_decoration(N, K, T, tasks):
    donuts = [0] * N
    for l, r, x in tasks:
        for i in range(l-1, r):
            if donuts[i] == 0:
                donuts[i] = x
    
    unique_tasks = set(donuts)
    if 0 in unique_tasks:
        unique_tasks.remove(0)
    
    return len(unique_tasks)