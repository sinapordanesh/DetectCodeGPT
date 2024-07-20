def identify_group_members(datasets):
    for dataset in datasets:
        n = int(dataset[0])
        groups = dataset[1:]

        group_members = {}
        for group in groups:
            group_name, members = group.split(':')
            members = members[:-1].split(',')

            group_members[group_name] = set()
            for member in members:
                if member in group_members:
                    group_members[group_name] = group_members[group_name].union(group_members[member])
                else:
                    group_members[group_name].add(member)

        first_group_members = len(group_members[groups[0].split(':')[0]])
        print(first_group_members)