def main():
    s = input()
    last_s = s[1]
    second_last_s = s[0]
    if last_s == second_last_s:
        print(1,2)
        exit()
    l = len(s)
    for i in range(2,l):
        if second_last_s == s[i]:
            print(i-1,i+1)
            exit()
        elif last_s == s[i]:
            print(i,i+1)
            exit()
        last_s = s[i]
        second_last_s = s[i-1]

    print(-1,-1)





if __name__ == "__main__":
    main()