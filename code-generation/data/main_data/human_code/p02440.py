
def run():
    n = int(input())
    li = [int(x) for x in input().split()]
    assert(len(li) == n)

    q = int(input())
    for _ in range(q):
        com, b, e = [int(x) for x in input().split()]
        if com == 0:
            print(min(li[b:e]))
        elif com == 1:
            print(max(li[b:e]))
        else:
            raise ValueError('invalid command')


if __name__ == '__main__':
    run()

