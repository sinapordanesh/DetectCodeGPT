def balloon_collecting():
    while True:
        n = int(input())
        if n == 0:
            break
        balloons = []
        for _ in range(n):
            p, t = map(int, input().split())
            balloons.append((p, t))
        
        time = 0
        position = 0
        for i in range(n):
            p, t = balloons[i]
            distance = abs(p - position)
            time_to_reach = distance // (i + 1)
            time_to_reach += 1 if distance % (i + 1) != 0 else 0
            time_to_catch = t - time
            if time_to_catch < time_to_reach:
                print(f"NG {i + 1}")
                break
            time += time_to_reach
            position = p
        else:
            print(f"OK {time}")

balloon_collecting()