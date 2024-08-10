def inherit_spheres():
    while True:
        N = int(input())
        if N == 0:
            break
        spheres = []
        for _ in range(N):
            spheres.append(list(map(int, input().split())))

        transitions = []
        prev_connect = 0
        for z in range(36001):
            connect = 0
            for sphere in spheres:
                x, y, zc, r = sphere
                dist = (sphere[2] - z) ** 2
                if dist <= r ** 2:
                    connect += 1
            if connect != prev_connect:
                transitions.append(str(int(connect > prev_connect)))
            prev_connect = connect

        print(len(transitions))
        print("".join(transitions))
        
inherit_spheres()