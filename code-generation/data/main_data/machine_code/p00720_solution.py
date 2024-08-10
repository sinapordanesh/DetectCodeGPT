def earth_observation_simulation():
    while True:
        N, T, R = map(int, input().split())
        if N == 0 and T == 0 and R == 0:
            break
        
        robots = []
        for _ in range(N):
            nickname, *data = input().split()
            robots.append((nickname, list(map(int, data))))
        
        print('\n'.join(sorted([robot[0] for robot in robots]))) 

earth_observation_simulation()