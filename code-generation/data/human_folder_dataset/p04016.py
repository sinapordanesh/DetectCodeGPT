import sys
input = sys.stdin.readline

def digit_sum(n, b):
    if b == 1:
        return n
    res = 0
    while n > 0:
        res += n % b
        n //= b
    return res

def main():
    n = int(input())
    s = int(input())
    
    ans = -1
    if n == s:
        ans = n + 1
    else:
        for b in range(2, int(n**0.5) + 1):
            if digit_sum(n, b) == s:
                ans = b
                break
        
        else:
            for p in range(1, int(n**0.5)+1):
                b = (n - s) // p + 1
                if b >= 2 and digit_sum(n, b) == s:
                    if ans == -1:
                        ans = b
                    else:
                        ans = min(ans, b)
                
                if b >= 1 and digit_sum(n, b+1) == s:
                    if ans == -1:
                        ans = b+1
                    else:
                        ans = min(ans, b+1)

    print(ans)



if __name__ == "__main__":
    main()
