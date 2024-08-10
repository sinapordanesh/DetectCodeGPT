def main():
    A, B, C = map(int, input().split())
    print('Yes' if A + B - C >= 0 else 'No')


if __name__ == '__main__':
    main()
