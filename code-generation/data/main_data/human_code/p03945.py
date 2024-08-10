def main():
    S = input()
    ans = 0
    for i, s in enumerate(S):
        if i == 0:
            t = s
            continue
        if t == s:
            continue
        else:
            ans += 1
            t = s
    print(ans)
        
if __name__ == "__main__":
    main()
