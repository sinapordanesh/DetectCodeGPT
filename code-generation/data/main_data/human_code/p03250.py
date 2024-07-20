
url = "https://atcoder.jp//contests/abc110/tasks/abc110_a"

def main():
    t = list(map(int, input().split()))
    t.sort(reverse=True)

    print(t[0]*10 + t[1] + t[2])

if __name__ == '__main__':
    main()
