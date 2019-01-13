"""The main file of the recommender."""
import os
import pickle

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

import decision_instance


def recommend(data):
    """Recommend yes or no."""
    clf = DecisionTreeClassifier()
    with open(os.path.join('models', 'DT.pkl'), 'rb') as file:
        clf = pickle.load(file)
    df_data = pd.DataFrame(data=data, columns=data.keys())
    print('Analyzing')
    print(df_data)
    result = clf.predict(df_data)
    print('The result is: {}'.format(result))
    return result


if __name__ == '__main__':
    instance = decision_instance.Instance()
    keys = instance.header().split(',')
    keys.remove('idx')
    values = []
    for key in keys:
        values.append(input('Please insert {}: '.format(key)))
    _data = {key: [value] for key, value in zip(keys, values)}
    recommend(_data)
