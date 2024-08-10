def max_discs_removed(data):
    while True:
        discs = data[:data.index(0)]
        data = data[data.index(0)+1:]
        if discs == []:
            break
        discs_dict = {}
        for disc in discs:
            if disc[3] not in discs_dict:
                discs_dict[disc[3]] = []
            discs_dict[disc[3]].append(disc)
        count = 0
        for key in discs_dict:
            count += len(discs_dict[key]) // 2
        print(count)