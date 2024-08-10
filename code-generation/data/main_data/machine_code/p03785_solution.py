def minimum_required_buses(N, C, K, arrivals):
    arrivals.sort()
    buses = 0
    current_bus_passengers = 0
    current_bus_departure_time = 0
    
    for arrival_time in arrivals:
        if current_bus_passengers == C or arrival_time > current_bus_departure_time:
            buses += 1
            current_bus_passengers = 0
            current_bus_departure_time = arrival_time + K
        
        current_bus_passengers += 1
    
    return buses

# Sample Input 1
print(minimum_required_buses(5, 3, 5, [1, 2, 3, 6, 12]))

# Sample Input 2
print(minimum_required_buses(6, 3, 3, [7, 6, 2, 8, 10, 6]))