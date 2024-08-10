def solve():
    from sys import stdin
    f_i = stdin
    
    # function to update distance between switch and computer
    def dfs(sw_id, prev, dist):
        switch[sw_id].append(dist)
        for next_sw in adj[sw_id]:
            if next_sw != prev:
                dfs(next_sw, sw_id, dist + 1)
    
    while True:
        N = int(f_i.readline())
        if N == 0:
            break
        
        # distance table of computers
        dist_tbl = [list(map(int, f_i.readline().split())) for i in range(N)]
        
        switch = [[1]] # switch[sw][com]: distance between sw and com
        degree = [1]
        adj = [[]] # adjacency list of switches
        
        for dt_i in dist_tbl[1:]:
            # try to connect a computer to an existing switch
            for m, sw_m in enumerate(switch):
                for dist_j, dt_ij in zip(sw_m, dt_i):
                    if dist_j != dt_ij - 1:
                        break
                else: # found a switch to connect a computer
                    degree[m] += 1
                    dfs(m, m, 1)
                    break
                continue
            else: # no switch to connect
                # find an existing switch to connect additional switch to
                for m, sw_m in enumerate(switch):
                    g = (x - y for x, y in zip(dt_i, sw_m))
                    diff = next(g)
                    for d in g:
                        if d != diff:
                            break
                    else:
                        break
                
                # first additional switch
                sw = len(switch)
                switch.append([dist + 1 for dist in switch[m]])
                adj[m].append(sw)
                adj.append([m])
                degree[m] += 1
                degree.append(1)
                
                # second and subsequent additional switches
                for i in range(2, diff):
                    switch.append([dist + i for dist in switch[m]])
                    adj[sw].append(sw + 1)
                    adj.append([sw])
                    degree[sw] += 1
                    degree.append(1)
                    sw += 1
                
                # connect a computer to the last added switch
                degree[sw] += 1
                dfs(sw, sw, 1)
                
        degree.sort()
        print(' '.join(map(str, degree)))

solve()
