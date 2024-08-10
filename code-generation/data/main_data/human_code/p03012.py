
url = "https://atcoder.jp//contests/abc129/tasks/abc129_b"

def main():
    n = int(input())
    t = list(map(int, input().split()))
    ans = 1000000000
    sums = sum(t)
    for v in t:
        sums -= v
        ans = min(abs((sum(t)-sums)-sums), ans)
    print(ans)


if __name__ == '__main__':
    main()
