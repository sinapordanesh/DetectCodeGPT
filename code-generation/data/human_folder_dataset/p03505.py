def main():
    k,a,b=map(int,input().split())
    if a<=b:
        if a>=k:
            print(1)
        else:
            print(-1)
        return
    print(((k-b-1)//(a-b)+1)*2-1)
    
    
main()