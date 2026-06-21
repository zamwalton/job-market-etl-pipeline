import pandas as pd
def extract_data():
    file_path = "C:/z/job pipeline/data/raw/jobs.csv"


    df = pd.read_csv(file_path)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())