def is_mirror_string(S):
    return "Yes" if S == S[::-1].replace('b', 'd').replace('d', 'b').replace('p', 'q').replace('q', 'p') else "No"