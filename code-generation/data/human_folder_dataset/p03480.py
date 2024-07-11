def main():
    S = input()
    l = len(S)
    ans = l
    #データ加工
    for i, s in enumerate(S[1:]):
        if s != S[i]:
            ans = min(ans, max(i+1, l-1-i))
    print(ans)
    
main()