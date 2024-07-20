def main():
    s = input()
    c = "CODEFESTIVAL2016"
    cnt = 0

    for i in range(len(s)):
        if s[i] != c[i]:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
