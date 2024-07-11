def main():
    r, d, x = list(map(int, input().split()))
    ans = x
    for i in range(1, 11):
        ans = (r*ans)-d
        print(ans)

if __name__ == '__main__':
    main()