def bamboo_blossoms(m, n):
    if m == 0 and n == 0:
        return
    
    result = 0
    while n > 0:
        result += m
        n -= 1

    print(result)
    
    bamboo_blossoms(m, n)

# Sample Input
bamboo_blossoms(3, 1)
bamboo_blossoms(3, 4)
bamboo_blossoms(10, 20)
bamboo_blossoms(100, 50)
bamboo_blossoms(2, 500000)
bamboo_blossoms(0, 0)