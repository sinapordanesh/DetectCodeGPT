def rearrange_matrix():
    H, W = map(int, input().split())
    matrix = [input() for _ in range(H)]
    
    count_odd = 0
    count_even = 0
    
    for row in matrix:
        for char in set(row):
            if row.count(char) % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    
    if H % 2 == 0 and W % 2 == 0:
        if count_odd == 0:
            print("Yes")
        else:
            print("No")
    elif H % 2 == 0 or W % 2 == 0:
        if count_odd <= H // 2 * W // 2:
            print("Yes")
        else:
            print("No")
    else:
        if count_odd == 1 and count_even == H*W - 1:
            print("Yes")
        else:
            print("No")

rearrange_matrix()