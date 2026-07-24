import pandas as pd

df = pd.read_csv("dataset/data.csv")

print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

print(df.duplicated().sum())