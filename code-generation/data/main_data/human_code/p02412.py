def main():

    while True:
        n, x = tuple(map(int, input().split()))
        pattern = 0

        if n == x == 0:
            break
        else:
            for a in range(1, n+1):
                for b in range(1, a):
                    for c in range(1, b):
                        pattern += 1 if a + b + c == x and a > b > c else 0
            print(pattern)
                            

if __name__ == '__main__':
    main()
