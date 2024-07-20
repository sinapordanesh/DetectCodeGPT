def safe_area():
    while True:
        W, H, N, R = map(int, input().split())
        if W == 0 and H == 0 and N == 0 and R == 0:
            break
        for _ in range(N):
            x1, y1, x2, y2, t = map(int, input().split())
        print("No" if N > 0 else "Yes") 

safe_area()