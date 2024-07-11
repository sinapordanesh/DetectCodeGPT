def main():
    n, k = map(int, input().split())
    results = tuple(map(int, input().split()))

    for i in range(n-k):
        print('Yes' if results[i] < results[i+k] else 'No')



if __name__ == '__main__':
    main()
