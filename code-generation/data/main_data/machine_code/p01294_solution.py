def for_the_peace(datasets):
    for data in datasets:
        n, d = data[0]
        countries = data[1:]
        for country in countries:
            m = country[0]
            capabilities = country[1:]
            potential = sum(capabilities)
            if max(potential) - min(potential) > d:
                print("No")
                continue
        print("Yes")