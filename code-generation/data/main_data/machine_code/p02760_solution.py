def check_bingo():
    bingo_card = [list(map(int, input().split())) for _ in range(3)]
    n = int(input())
    marked_numbers = [int(input()) for _ in range(n)]
    
    for i in range(3):
        if all(num in marked_numbers for num in bingo_card[i]):
            return "Yes"
        if all(num in marked_numbers for num in [bingo_card[j][i] for j in range(3)]):
            return "Yes"
    
    if all(bingo_card[i][i] in marked_numbers for i in range(3)) or all(bingo_card[i][2-i] in marked_numbers for i in range(3)):
        return "Yes"
    
    return "No"

print(check_bingo())