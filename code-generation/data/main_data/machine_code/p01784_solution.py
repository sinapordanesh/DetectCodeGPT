def parentheses(n, strings):
    total_open = 0
    total_close = 0
    for s in strings:
        open_count = s.count("(")
        close_count = s.count(")")
        total_open += open_count
        total_close += close_count
    
    if total_open == total_close and total_open % 2 == 0:
        return "Yes"
    else:
        return "No"