def same_face(xpy_p, d_p, l_p, xqy_q, d_q, l_q):
    faces = {('BC', 'CD', 'DB'): 'YES', ('CD', 'DB', 'BC'): 'NO', ('DB', 'BC', 'CD'): 'NO'}
    return faces[(xpy_p, xqy_q)] if d_p % 60 == d_q % 60 else faces[(xqy_q, xpy_p)]

# Test cases
print(same_face('CD', 30, 1, 'DB', 30, 1))
print(same_face('BC', 1, 1, 'DB', 59, 1))
print(same_face('BC', 29, 20, 'BC', 32, 20))