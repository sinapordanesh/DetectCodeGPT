def minimum_carpets():
    while True:
        W, H = map(int, input().split())
        if W == 0 and H == 0:
            break
        panels = [list(map(int, input().split())) for _ in range(H)]
        count = 0
        for i in range(H):
            for j in range(W):
                if panels[i][j] == 1:
                    count += 1
        print((count + 8) // 9)
        
minimum_carpets()