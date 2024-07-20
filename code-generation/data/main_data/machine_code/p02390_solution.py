def convert_seconds_to_hms(S):
    h = S // 3600
    m = (S % 3600) // 60
    s = S % 60
    return f"{h}:{m}:{s}"

S = int(input())
print(convert_seconds_to_hms(S))