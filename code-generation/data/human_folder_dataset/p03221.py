def main():
    n, m = map(int, input().split())
    inlis = []

    for i in range(m):
        p, y = map(int, input().split())
        inlis.append([i+1, p, y])

    inlis = sorted(inlis, key = lambda x:x[2])
    anslis = []
    tmpdic = dict()

    for i in range(m):
        j, p, y = inlis[i][0], inlis[i][1], inlis[i][2]
        
        if p not in tmpdic:
            tmpdic[p] = 1
        else:
            tmpdic[p] += 1
        
        num = str(tmpdic[p]).zfill(6)
        ken = str(p).zfill(6)

        ans = ken + num
        anslis.append([j,ans])
    
    anslis = sorted(anslis, key = lambda x:x[0])

    for [city, num] in anslis:
        print(num)


    



if __name__ == "__main__":
    main()
