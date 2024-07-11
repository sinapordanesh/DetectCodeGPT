from collections import defaultdict


def main():
    # 同じ文字を2つつなげると回文になるので、最低限隣り合う文字が全部異なる必要がある。
    # また、abaのように、2つ先で一致してしまってもこれも回文になるのでNG。
    # となると結局「abcabc...」みたいに巡回する形の文字列しか回文回避の方法はない。
    # こういう巡回する形の文字列を作るには、a,b,cの数の最大と最小の差が1以内であればOK。
    S = input()
    counter = defaultdict(int)
    for s in S:
        counter[s] += 1
    counts = [counter[s] for s in "abc"]
    if max(counts) - min(counts) <= 1:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()