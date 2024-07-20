def max_elements_in_S(T, testcases):
    result = []
    for i in range(T):
        x_A, y_A, r_A, x_B, y_B, r_B = testcases[i]
        
        d = ((x_A - x_B)**2 + (y_A - y_B)**2)**0.5
        theta = 2 * acos((r_A**2 + d**2 - r_B**2) / (2 * r_A * d))
        num_elements = int(pi / theta)
        
        result.append(num_elements)
    
    return result