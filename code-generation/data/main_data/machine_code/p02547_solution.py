def check_doublets(N, rolls):
    for i in range(N-2):
        if rolls[i][0] == rolls[i][1] and rolls[i+1][0] == rolls[i+1][1] and rolls[i+2][0] == rolls[i+2][1]:
            return "Yes"
    return "No"