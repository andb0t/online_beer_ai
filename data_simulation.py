"""Create training data."""
import os

import decision_instance


datasets = {"train.csv": 1000, "test.csv": 100}


for dataset, n_data in datasets.items():
    instance = decision_instance.Instance('train' in dataset)
    with open(os.path.join('data', dataset), 'w') as file:
        print(instance.header(), file=file)
        for entry in range(n_data):
            data = {'idx': entry, 'time': 24, 'n_ppl': 10}
            if 'train' in dataset:
                data['decision'] = 1
            instance.fill(data)
            print(instance.csv(), file=file)
