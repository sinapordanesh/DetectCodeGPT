def main():
    n = int(input())
    cnt = 0
    for i in [25, 10, 5, 1]:
        cnt += n // i
        n = n % i
    print(cnt)

if __name__ == '__main__':
    main()
