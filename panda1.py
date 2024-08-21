import pandas as pd
df = pd.read_csv(r'C:\Users\tarin\OneDrive\Documents\stddataset.csv')
print(df)
print(df.head())
print(df.describe())
print(df.isnull().sum())
print(df.shape)
