def main():
    n = int(input())
    A = input_list()
    B = input_list()
    C = [A[i] - B[i] for i in range(n)]
    s = sum(C)
    if s < 0:
        print(-1)
        exit()
    C.sort()
    ans = 0
    for i in range(n):
        if C[i] < 0:
            continue
        elif C[i] <= s:
            ans += 1
            s -= C[i]
        else:
            break
    print(n-ans)
    

def input_list():
    return list(map(int, input().split()))

if __name__ == "__main__":
    main()