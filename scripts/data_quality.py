import pandas as pd

df = pd.read_csv("../data/processed/jobs_clean.csv")

print("Null Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())