def main():

    A, B = input().split()
    A = int(A)
    B100 = int(B[0] + B[2:])
    print(A*B100//100)


if __name__ == "__main__":
    main()
