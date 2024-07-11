# coding: utf-8


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    B = [0] * 9
    mn, mx = 0, 0

    for a in A:
        a //= 400
        if a > 7: a = 8
        B[a] += 1
    
    for i in range(8):
        if B[i] > 0: mn += 1
    
    mx = mn + B[8]
    if mn == 0: mn += 1

    print(mn, mx)

if __name__ == "__main__":
    main()
