

def run():
    n = int(input())
    li = input().split()
    assert(len(li) == n)

    q = int(input())
    for _ in range(q):
        b, e = [int(x) for x in input().split()]
        li = li[:b] + list(reversed(li[b:e])) + li[e:]

    print(" ".join(li))


if __name__ == '__main__':
    run()

