import pandas as pd
import numpy as np
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')
df['age'].fillna(df['age'].mean(), inplace=True)
df['sex'] = df['sex'].map({'male': 0, 'female': 1})
df[['age', 'fare']] = (df[['age', 'fare']] - df[['age', 'fare']].min()) / (df[['age', 'fare']].max() - df[['age', 'fare']].min())
print(df.head())
print(df.describe())
