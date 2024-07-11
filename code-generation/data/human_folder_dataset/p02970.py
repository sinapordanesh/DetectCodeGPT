def main():
    n, d = list(map(int, input().split()))
    a, s = divmod(n, (d*2)+1)
    print(a) if s == 0 else print(a+1)


if __name__ == '__main__':
    main()