def diceIV():
    n = int(input())
    dices = [list(map(int, input().split())) for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1, n):
            if set(dices[i]) == set(dices[j]):
                print("No")
                return
    print("Yes")

diceIV()