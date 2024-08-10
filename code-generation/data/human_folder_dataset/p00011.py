def run():
    w = [i + 1 for i in range(int(input()))]
    n = int(input())
    for _ in range(n):
        s1, s2 = list(map(int, input().split(',')))
        w[s1-1], w[s2-1] = w[s2-1], w[s1-1]
    print('\n'.join([str(_w) for _w in w]))

if __name__ == '__main__':
    run()


