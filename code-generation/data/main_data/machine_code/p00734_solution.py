def equal_total_scores():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        
        taro_cards = [int(input()) for _ in range(n)]
        hanako_cards = [int(input()) for _ in range(m)]
        
        total_taro = sum(taro_cards)
        total_hanako = sum(hanako_cards)
        
        for i in range(n):
            for j in range(m):
                if (total_taro - taro_cards[i] + hanako_cards[j]) == (total_hanako - hanako_cards[j] + taro_cards[i]):
                    print(f"{taro_cards[i]} {hanako_cards[j]}")
                    break
            else:
                continue
            break
        else:
            print("-1")

equal_total_scores()