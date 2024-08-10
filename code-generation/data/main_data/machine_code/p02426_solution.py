def bit_mask(n, masks, q, queries):
    state = [0] * 64
    
    def test(i):
        return state[i]
    
    def set(m):
        for bit in masks[m][1:]:
            state[bit] = 1
            
    def clear(m):
        for bit in masks[m][1:]:
            state[bit] = 0
            
    def flip(m):
        for bit in masks[m][1:]:
            state[bit] = 1 - state[bit]
    
    def all(m):
        for bit in masks[m][1:]:
            if state[bit] == 0:
                return 0
        return 1
    
    def any(m):
        for bit in masks[m][1:]:
            if state[bit] == 1:
                return 1
        return 0
    
    def none(m):
        for bit in masks[m][1:]:
            if state[bit] == 1:
                return 0
        return 1
    
    def count(m):
        count = 0
        for bit in masks[m][1:]:
            if state[bit] == 1:
                count += 1
        return count
    
    def val(m):
        value = 0
        for bit in masks[m][1:]:
            value += 2**bit
        return value
    
    operations = [test, set, clear, flip, all, any, none, count, val]
    
    output = []
    
    for query in queries:
        operation, argument = query
        result = operations[operation](argument)
        output.append(result)
    
    return output

# Sample Input
n = 3
masks = [[3, 0, 1, 3], [1, 3], [3, 0, 1, 2]]
q = 8
queries = [[1, 0], [2, 1], [3, 1], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2]]

# Sample Output
print(*bit_mask(n, masks, q, queries))