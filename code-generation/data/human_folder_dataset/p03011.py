
url = "https://atcoder.jp//contests/abc129/tasks/abc129_a"

def main():
    p, q, r = list(map(int, input().split()))
    print(sum([p,q,r]) - max(p,q,r))

if __name__ == '__main__':
    main()
