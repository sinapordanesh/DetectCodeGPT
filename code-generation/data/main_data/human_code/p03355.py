def main():
    S = input()
    K = int(input())
    Sset = set()
    for i in range(len(S)):
        for j in range(1, K+1):
            Sset.add(S[i:i+j])
    Slist = list(Sset)
    Slist.sort()
    # print(Slist)
    print(Slist[K-1])

if __name__ == "__main__":
    main()
