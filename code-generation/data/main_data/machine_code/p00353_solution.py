def calculate_borrow_amount(m, f, b):
    if m + f >= b:
        return max(0, b - m)
    else:
        return "NA"