import itertools


def main():
    a = 'abcdefghijklmnopqrstuvwxyz'
    s = input()

    if len(s) < 26:
        for v in s:
            a = a.replace(v, '')
        print(s + a[0])
    elif s == a[::-1]:
        print(-1)
    else:
        for i in (range(25))[::-1]:
            if s[i] < s[i+1]:
                for j in range(i+1, len(s))[::-1]:
                    if s[i] < s[j]:
                        print(s[:i]+s[j])
                        exit()


def input_list():
    return list(map(int, input().split()))

if __name__ == "__main__":
    main()