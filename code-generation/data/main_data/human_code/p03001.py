def main():

    W, H, x, y = [int(i) for i in input().split()]

    if (W/2 == x) & (H/2 == y):
        j = 1
    else:
        j = 0
    print(W*H/2, j)


if __name__ == "__main__":
    main()
