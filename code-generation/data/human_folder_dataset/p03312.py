import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0]*(n+1)

    for i in range(n):
        s[i+1] += s[i] + a[i]
    
    ans = int(1e15)
    for i in range(n):
        sub = []
        for l, r, ll, rr in zip([0, i], [i, n], [0, i], [i, n]):
            while r-l > 1:
                k = (r+l) // 2
                if s[k] - s[ll] < s[rr] - s[k]:
                    l = k
                else:
                    r = k

            if abs(s[ll] + s[rr] - s[l]*2) > abs(s[ll] + s[rr] - s[r]*2):
                k = r
            else:
                k = l
            sub.append(s[k] - s[ll])
            sub.append(s[rr] - s[k])
        judge = max(sub) - min(sub)
        ans = min(ans, judge)
    
    print(ans)


    
if __name__ == "__main__":
    main()

