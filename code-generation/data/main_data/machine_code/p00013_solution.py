def switching_railroad_cars():
    cars = []
    while True:
        car_number = int(input())
        if car_number == 0:
            break
        cars.append(car_number)
    
    for car in reversed(cars):
        if car == 0:
            print(cars.pop())
            
switching_railroad_cars()