def read_a(n, m):
    A = []
    for _ in range(0, n):
        A.append([int(x) for x in input().split()])

    return A

def read_b(m):
    B = []
    for _ in range(0, m):
        B.append(int(input()))

    return B

def multiply(A, B):
    C = []
    for a in A:
        C.append(sum(map(lambda x, y:x*y, a, B)))

    return C

def main():
    n, m = [int(x) for x in input().split()]

    A = read_a(n, m)
    B = read_b(m)
    C = multiply(A, B)

    print("\n".join([str(x) for x in C]))

if __name__ == '__main__':
    main()

