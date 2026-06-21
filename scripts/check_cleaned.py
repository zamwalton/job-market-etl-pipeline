import pandas as pd

df = pd.read_csv("../data/processed/jobs_clean.csv")

print(df.isnull().sum())