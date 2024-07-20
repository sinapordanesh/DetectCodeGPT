def accelerated_railgun():
    while True:
        D = float(input())
        if D == 0:
            break
        px, py, vx, vy = map(float, input().split())
        
        distance = 0
        while True:
            if px**2 + py**2 <= 1.0:
                print(f'{distance:.8f}')
                break
            if distance >= D:
                print('impossible')
                break
            a = (vx**2 + vy**2)**0.5
            t = ((px*vx + py*vy)/a - ((px*vx + py*vy)/a)**2 + 1 - (px**2 + py**2 - 1))/a
            x = px + vx*t
            y = py + vy*t
            d = ((x-px)**2 + (y-py)**2)**0.5
            distance += d
            px, py = x, y

accelerated_railgun()