def days_until_next_sunday(S):
    if S == "SUN":
        return 7
    elif S == "MON":
        return 6
    elif S == "TUE":
        return 5
    elif S == "WED":
        return 4
    elif S == "THU":
        return 3
    elif S == "FRI":
        return 2
    elif S == "SAT":
        return 1

S = input().strip()
print(days_until_next_sunday(S))