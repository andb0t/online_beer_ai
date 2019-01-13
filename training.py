"""Train the classifier."""
import os
import pickle

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

import decision_instance


file = os.path.join('data', 'train.csv')
df_train = pd.read_csv(file, index_col=0)
file = os.path.join('data', 'test.csv')
df_test = pd.read_csv(file, index_col=0)

y_train = df_train['decision']
X_train = df_train.drop(['decision'], axis=1)
y_test = df_test['decision']
X_test = df_test.drop(['decision'], axis=1)

clf = DecisionTreeClassifier(max_depth=3)
clf.fit(X_train, y_train)
score = clf.score(X_test, y_test)
print('Final score', score)

with open(os.path.join('models', 'DT.pkl'), 'wb') as file:
    pickle.dump(clf, file)
