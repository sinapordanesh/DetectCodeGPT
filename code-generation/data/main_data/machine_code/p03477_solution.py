def balance_scale(A, B, C, D):
    left_weight = A + B
    right_weight = C + D
    
    if left_weight > right_weight:
        print("Left")
    elif left_weight < right_weight:
        print("Right")
    else:
        print("Balanced")