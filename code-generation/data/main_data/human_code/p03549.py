def main():
    N, M = map(int, input().split())
    ans = (1900*M + 100*(N - M))*pow(2, M)
    print(ans)

if __name__ == "__main__":
    main()
