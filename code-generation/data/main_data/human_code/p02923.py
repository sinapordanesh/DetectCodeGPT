# coding: utf-8

def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    tmp = 0
    tmp_h = H[0]

    for i in range(1, N):
        if H[i] <= tmp_h:
            tmp += 1
        else :
            ans = max(ans, tmp)
            tmp = 0
        tmp_h = H[i]

    ans = max(ans, tmp)

    print(ans)

if __name__ == "__main__":
    main()
