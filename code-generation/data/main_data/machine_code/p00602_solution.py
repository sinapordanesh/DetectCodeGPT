def connected_subsets(input_data):
    subsets = []
    for data in input_data:
        V, d = data
        fib = [1, 1]
        while True:
            next_fib = fib[-1] + fib[-2]
            fib.append(next_fib % 1001)
            if next_fib % 1001 == 1 and fib[-2] == 1:
                break
        
        connected = set()
        for i in range(1, V+1):
            for j in range(1, V+1):
                if abs(fib[i] - fib[j]) < d:
                    connected.add(i)
                    connected.add(j)
        
        subsets.append(len(connected))
    
    return subsets

# Sample input
print(connected_subsets([(5, 5), (50, 1), (13, 13)]))