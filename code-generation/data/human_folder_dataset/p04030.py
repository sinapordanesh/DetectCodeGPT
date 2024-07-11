def main():
    s = str(input())

    ans = []
    for val in s :
        if val == "B" and ans == [] :
            pass
        elif val == "B" and ans != [] :
            ans.pop(-1)
        else :
            ans.append(val)

    ans_str = ""
    for val in ans :
        ans_str = ans_str + val

    print(ans_str)



if __name__ == '__main__':
    main()
