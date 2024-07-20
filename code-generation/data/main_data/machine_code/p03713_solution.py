def min_chocolate_difference():
    H, W = map(int, input().split())
    if H % 3 == 0 or W % 3 == 0:
        print(0)
    else:
        ans = min(min(H, W//3), min(W, H//3), min((H+1)//2, (W+1)//3), min((H+2)//3, W))
        print(W*H - ans*max(W//3, H//3, (H+1)//3, (W+1)//3, (H+2)//3))

min_chocolate_difference()