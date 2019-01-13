"""Create training data."""
import os
import random

import decision_instance


datasets = {"train.csv": 1000, "test.csv": 100}


def decide(data):
    if data['n_ppl'] == 1:
        return 0
    if data['n_ppl'] > 10:
        return 1
    if 19 > data['time'] > 23:
        return 1
    if 2 > data['time'] > 10:
        return 0
    return random.randint(0, 1)


for dataset, n_data in datasets.items():
    yes_count = 0
    instance = decision_instance.Instance(True)
    with open(os.path.join('data', dataset), 'w') as file:
        print(instance.header(), file=file)
        for entry in range(n_data):
            data = {'idx': entry,
                    'time': random.randint(0, 24),
                    'n_ppl': random.randint(1, 25)}
            if instance.truth:
                result = decide(data)
                data['decision'] = result
                yes_count += result
            instance.fill(data)
            print(instance.csv(), file=file)
    yes_frac = yes_count / n_data
    print('Wrote {} ({:.0%}) yes decisions in file {}'.format(yes_count, yes_frac, dataset))
