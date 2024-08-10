def rearrange_strings(s, t):
    s_sorted = ''.join(sorted(s))
    t_sorted = ''.join(sorted(t))
    return "Yes" if s_sorted < t_sorted else "No"