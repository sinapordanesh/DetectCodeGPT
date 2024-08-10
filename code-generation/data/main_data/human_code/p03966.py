def main():
    N = int(input())
    a = 1
    t = 1
    for _ in range(N):
        T, A = map(int, input().split())
        if t <= T and a <= A:
            t = T
            a = A
        elif t <= T and a > A:
            tmp = a // A
            if a % A != 0:
                tmp += 1
            t = T * tmp
            a = A * tmp
        elif t > T and a <= A:
            tmp = t // T
            if t % T != 0:
                tmp += 1
            t = T * tmp
            a = A * tmp
        else:
            tmp_A = a // A
            if a % A != 0:
                tmp_A += 1
            tmp_T = t // T
            if t % T != 0:
                tmp_T += 1
            tmp = max(tmp_A, tmp_T)
            t = T * tmp
            a = A * tmp
    print(a + t)



if __name__ == "__main__":
    main()