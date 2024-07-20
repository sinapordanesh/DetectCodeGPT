def algae_growth(r, D, x_2000):
    x_values = []
    x_values.append(r*x_2000 - D)
    for i in range(2001, 2011):
        x_values.append(r*x_values[-1] - D)
    for x in x_values:
        print(x)

algae_growth(2, 10, 20)