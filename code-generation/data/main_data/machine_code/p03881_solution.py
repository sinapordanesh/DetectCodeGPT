def tourist_wins(p1, p2, p3, p4, p5, p6, q1, q2, q3, q4, q5, q6):
    p_red = (p1 + p2 + p3 + p4 + p5 + p6) / 100
    p_blue = (q1 + q2 + q3 + q4 + q5 + q6) / 100
    
    if p1 + p2 + p3 + p4 <= q5 + q6:
        return 1.0
    elif p5 + p6 <= q1 + q2 + q3 + q4:
        return 0.0
    else:
        return (p_blue * (q5 + q6) + p_red * (p1 + p2 + p3 + p4)) / 100

# Sample Input 1
print(tourist_wins(25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 50, 50))

# Sample Input 2
print(tourist_wins(10, 20, 20, 10, 20, 20, 20, 20, 20, 10, 10, 20))