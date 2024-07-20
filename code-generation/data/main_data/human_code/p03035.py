def main():
    a, b = list(map(int, input().split()))
    ans = 0
    if a >= 13:
        ans = b
    elif 6 <= a <= 12:
        ans = b//2
    print(ans)

if __name__ == '__main__':
    main()
