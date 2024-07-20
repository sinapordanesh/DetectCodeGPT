def fill_square_grid(H, W, A, B):
    if 2 * A > W or 2 * B > H:
        print(-1)
    else:
        for i in range(H):
            row = ""
            for j in range(W):
                if i < B:
                    if j < A:
                        row += "1"
                    else:
                        row += "0"
                else:
                    if j < A:
                        row += "0"
                    else:
                        row += "1"
            print(row)

# Sample Input 1
fill_square_grid(3, 3, 1, 1)

# Sample Input 2
fill_square_grid(1, 5, 2, 0)