def infected_computer():
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        
        infected = {1}
        for _ in range(M):
            t, s, d = map(int, input().split())
            if s in infected:
                infected.add(d)
        
        print(len(infected))

infected_computer()