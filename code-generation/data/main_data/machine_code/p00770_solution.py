import sympy

def descending_route(total_caves, start_cave):
    def is_prime(num):
        return sympy.isprime(num)
    
    def get_neighbors(cave_num, total_caves):
        neighbors = set()
        if cave_num - 1 > 0:
            neighbors.add(cave_num - 1)
        if cave_num + 1 <= total_caves:
            neighbors.add(cave_num + 1)
        if cave_num + 1 + int((cave_num - 1) ** 0.5) <= total_caves:
            neighbors.add(cave_num + 1 + int((cave_num - 1) ** 0.5))
        return neighbors
    
    path = []
    current_cave = start_cave
    prime_caves = set()
    
    while current_cave not in prime_caves:
        path.append(current_cave)
        if is_prime(current_cave):
            prime_caves.add(current_cave)
        
        neighbors = get_neighbors(current_cave, total_caves)
        max_prime_neighbor = None
        max_prime_count = 0
        
        for neighbor in neighbors:
            prime_count = 0
            if is_prime(neighbor):
                prime_count += 1
            path_copy = path.copy()
            path_copy.append(neighbor)
            while is_prime(neighbor):
                prime_count += 1
                neighbor += int((neighbor - 1) ** 0.5) + 1
                if neighbor > total_caves:
                    break
            if prime_count > max_prime_count:
                max_prime_count = prime_count
                max_prime_neighbor = neighbor - 1
        
        if max_prime_neighbor is None:
            break
        else:
            current_cave = max_prime_neighbor
    
    prime_count = len(prime_caves)
    last_prime_cave = max(prime_caves)
    
    return prime_count, last_prime_cave

# Sample Input
print(descending_route(49, 22))
print(descending_route(46, 37))
print(descending_route(42, 23))
print(descending_route(945, 561))
print(descending_route(1081, 681))
print(descending_route(1056, 452))
print(descending_route(1042, 862))
print(descending_route(973, 677))
print(descending_route(1000000, 1000000))