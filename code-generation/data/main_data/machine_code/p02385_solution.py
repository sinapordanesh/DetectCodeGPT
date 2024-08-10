def check_identical_dices(dice1, dice2):
    if dice1 == dice2:
        print("Yes")
    else:
        print("No")

dice1 = list(map(int, input().split()))
dice2 = list(map(int, input().split()))

check_identical_dices(dice1, dice2)