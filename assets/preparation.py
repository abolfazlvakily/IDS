import pandas as pd



data = pd.read_csv("assets/data/Train_data.csv")
columns_names = pd.DataFrame({'column': data.columns})

X_test = pd.read_csv('assets/data/X_test.csv').drop(['Unnamed: 0'], axis=1)
y_test = pd.read_csv('assets/data/y_test.csv')['class']
test = pd.read_csv('assets/data/test.csv').drop(['Unnamed: 0'], axis=1)
