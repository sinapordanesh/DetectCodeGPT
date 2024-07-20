def calculate_fuel(input_list):
    def cubic(n):
        return n**3
    
    def tetrahedral(n):
        return n*(n+1)*(n+2)//6
    
    def calculate_max_fuel_balls(num):
        max_fuel = 0
        for i in range(num):
            for j in range(num):
                c = cubic(i)
                t = tetrahedral(j)
                if c + t <= num and c + t > max_fuel:
                    max_fuel = c + t
        return max_fuel
    
    result = []
    for num in input_list:
        if num == 0:
            break
        result.append(calculate_max_fuel_balls(num))
    
    return result

# Sample Input
input_list = [100, 64, 50, 20, 151200, 0]
print(calculate_fuel(input_list))