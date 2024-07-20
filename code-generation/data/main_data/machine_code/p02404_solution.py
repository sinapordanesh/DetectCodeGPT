def print_frame():
    while True:
        H, W = map(int, input().split())
        if H == 0 and W == 0:
            break
        
        for i in range(H):
            if i == 0 or i == H - 1:
                print("#" * W)
            else:
                print("#" + "." * (W - 2) + "#")
        
        print()

print_frame()