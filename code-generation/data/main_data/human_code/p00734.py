def answer(n, m, taro, hanako):
    for t in sorted(taro):
        for h in sorted(hanako):
            if sum(taro) - t + h == sum(hanako) - h + t:
                return f'{t} {h}'
    return -1


while True:
    n, m = map(int, input().split()) # 組み込み関数input()は標準入力から読み込まれた1行を返す．
    if n == 0 and m == 0:
        break
    taro = []
    hanako = []
    for i in range(n):
        taro.append(int(input()))
    for i in range(m):
        hanako.append(int(input()))
    print(answer(n, m, taro, hanako))


