def baseball_simulation(n, datasets):
    for dataset in datasets:
        score = 0
        runners = 0
        outs = 0
        for event in dataset:
            if event == "HIT":
                if runners == 3:
                    score += 1
                else:
                    runners += 1
            elif event == "HOMERUN":
                score += runners + 1
                runners = 0
            elif event == "OUT":
                outs += 1
                if outs == 3:
                    break
        print(score)

n = 2
datasets = [["HIT", "OUT", "HOMERUN"], ["HIT", "HIT", "HOMERUN", "HIT", "OUT", "HIT", "HIT", "HIT", "HIT", "OUT", "HIT", "HIT", "OUT", "HIT", "OUT", "OUT"]]
baseball_simulation(n, datasets)