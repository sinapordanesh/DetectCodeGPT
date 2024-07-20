def stone_taking_game(N, piles):
    def floor_div(x, k):
        return x // k
    
    takahashi_turn = True
    while True:
        if all(pile[0] == 0 for pile in piles):
            return "Aoki"
        
        if takahashi_turn:
            for i in range(N):
                x, k = piles[i]
                if x > 0:
                    max_stones = floor_div(x, k)
                    for stones_removed in range(1, max_stones + 1):
                        piles_copy = piles.copy()
                        piles_copy[i] = (x - stones_removed, k)
                        if stone_taking_game(N, piles_copy) == "Takahashi":
                            return "Takahashi"
            return "Aoki"
        else:
            for i in range(N):
                x, k = piles[i]
                if x > 0:
                    max_stones = floor_div(x, k)
                    for stones_removed in range(1, max_stones + 1):
                        piles_copy = piles.copy()
                        piles_copy[i] = (x - stones_removed, k)
                        if stone_taking_game(N, piles_copy) == "Aoki":
                            return "Aoki"
            return "Takahashi"

N = int(input())
piles = [tuple(map(int, input().split())) for _ in range(N)]
print(stone_taking_game(N, piles))