import statistics

def get_data():
    data = int(input())
    return data

def get_data_list():
    data_list = input().split()
    for i, v in enumerate(data_list):
        data_list[i] = int(v)
    return data_list

def count_num_under_average(list_num, reverse_sorted_num_list, average_num):
    count = list_num
    for v in reverse_sorted_income_list:
        if v > average_num:
            count -= 1
        else:
            break
    return count


if __name__ == "__main__":
    while True:
        population = get_data()
        if population == 0:
            break
        income_list = get_data_list()
        reverse_sorted_income_list = sorted(income_list, reverse=True)
        average_income = statistics.mean(reverse_sorted_income_list)
        count = count_num_under_average(population, reverse_sorted_income_list, average_income)
        print(count)


