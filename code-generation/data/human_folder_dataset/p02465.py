def main():
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    s = sorted(set(a)-set(b))
    for c in s:print (c)



if __name__ == '__main__':
    main()


