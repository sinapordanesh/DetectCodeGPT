# coding: utf-8

def main():
    _, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    ans = 0

    for i in a:
        x -= i
        if x < 0:
            break
        else:
            ans += 1

    if x > 0 and ans > 0:
        ans -= 1

    print(ans)

if __name__ == "__main__":
    main()
