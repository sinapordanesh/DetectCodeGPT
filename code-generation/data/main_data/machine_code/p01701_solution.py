def detailed_direction_angle(direction):
    angle = 0
    n = direction.count("north") + direction.count("west")
    
    for i in range(n):
        if "north" in direction:
            angle -= 90 / (2 ** n)
            direction = direction.replace("north", "", 1)
        elif "west" in direction:
            angle += 90 / (2 ** n)
            direction = direction.replace("west", "", 1)
    
    if angle.is_integer():
        return int(angle)
    else:
        return f"{int(angle)}/{2}"
    
# Sample Input
print(detailed_direction_angle("north"))
print(detailed_direction_angle("west"))
print(detailed_direction_angle("northwest"))
print(detailed_direction_angle("northnorthwest"))
print(detailed_direction_angle("westwestwestnorth"))