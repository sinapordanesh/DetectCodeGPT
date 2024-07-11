
def run():
    n = int(input())
    li = [int(x) for x in input().split()]
    assert(len(li) == n)

    q = int(input())
    for _ in range(q):
        b, e, k = [int(x) for x in input().split()]
        print(li[b:e].count(k))


if __name__ == '__main__':
    run()

