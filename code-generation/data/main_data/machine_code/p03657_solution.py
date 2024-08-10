def cookies_distribution(A, B):
    total_cookies = A + B
    if total_cookies % 3 == 0 and A <= total_cookies // 3 and B <= total_cookies // 3:
        return "Possible"
    else:
        return "Impossible"