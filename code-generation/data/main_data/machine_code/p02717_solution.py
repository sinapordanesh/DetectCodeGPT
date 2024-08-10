def box_operation(X, Y, Z):
    A = X
    B = Y
    C = Z
    
    A, B = B, A
    A, C = C, A
    
    return f"{A} {B} {C}"