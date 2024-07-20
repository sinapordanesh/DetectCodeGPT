def main():
    s = input()
    flag = True

    for i in range(len(s)):
        if flag:
            if s[i] == "C":
                flag = False
        else:
            if s[i] == "F":
                print("Yes")
                exit()
    else:
        print("No")


if __name__ == "__main__":
    main()
