def main():
    n = int(input())
    al = list(map(int, input().split()))
    maxval = max(abs(max(al)), abs(min(al)))
    cost = []
    if len(list(set(al))) == 1 :
        print("0")
    else :
        k = -1
        for i in range(-100,100) :
            k += 1
            cost.append(0)
            for j in range(n) :
                cost[k] = cost[k] + (al[j] - i) ** 2
                #print(cost[i])
        print(min(cost))



if __name__ == '__main__':
    main()
