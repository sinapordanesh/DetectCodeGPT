def min_votes(dataset):
    def calculate_votes(district):
        if "[" not in district:
            return int(district)
        sub_districts = district.strip('[]').split('][')
        sub_votes = [calculate_votes(sub) for sub in sub_districts]
        return sum(sub_votes) // 2 + 1
    
    return calculate_votes(dataset)

n = int(input())
for _ in range(n):
    dataset = input()
    print(min_votes(dataset))