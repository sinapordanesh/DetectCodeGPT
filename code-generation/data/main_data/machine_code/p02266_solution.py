def areas_on_cross_section_diagram(s):
    areas = []
    area = 0
    stack = []
    
    for i in range(len(s)):
        if s[i] == "\\":
            stack.append(i)
        elif s[i] == "/" and stack:
            j = stack.pop()
            area += i - j
            current_area = i - j
            while areas and areas[-1][0] > j:
                current_area += areas.pop()[1]
            areas.append((j, current_area))
    
    result = [area]
    result.append(len(areas))
    for _, a in areas:
        result.append(a)
    
    return result

# Test the function
print(areas_on_cross_section_diagram("\\//"))
print(areas_on_cross_section_diagram("\\///\_/\/\\\\/_/\\///__\\\_\\/_\/_/\\"))