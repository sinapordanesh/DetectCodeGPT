import sys
input = sys.stdin.readline

def main():
    l = int(input())

    ll = l
    key = 0
    while ll > 0:
        key += 1
        ll //= 2
    
    ans = []
    for i in range(key-1):
        ans.append((i+1, i+2, 0))
        ans.append((i+1, i+2, pow(2, i)))
    
    l -= pow(2, key-1)
    l = bin(l)[2:]
    sub = pow(2, key-1)
    
    for i in range(len(l)):
        if l[i] == '1':
            ans.append((len(l)-i, key, sub))
            sub += pow(2, len(l)-i-1)
    

    print(key, len(ans))
    for a in ans:
        print(*a)




    
if __name__ == "__main__":
    main()

