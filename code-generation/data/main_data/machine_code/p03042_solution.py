
def check_date_format(S):
    if 1 <= int(S[:2]) <= 12 and 1 <= int(S[2:]) <= 12:
        return "AMBIGUOUS"
    elif 1 <= int(S[:2]) <= 12:
        return "MMYY"
    elif 1 <= int(S[2:]) <= 12:
        return "YYMM"
    else:
        return "NA"

S = input()
print(check_date_format(S))