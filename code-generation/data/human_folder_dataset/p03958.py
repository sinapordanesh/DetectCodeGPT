def main():
    K, T = list(map(int, input().split()))
    A = list(map(int, input().split()))
    max_a = max(A)
    print(max(0, 2 * max_a - 1 - K))


if __name__ == '__main__':
    main()