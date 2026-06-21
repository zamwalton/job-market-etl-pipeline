import pandas as pd
def transform_data():
    # Read raw data
    df = pd.read_csv("../data/raw/jobs.csv")

    print("Before Cleaning:")
    print(df.shape)

    # Remove rows where job title is missing
    df = df.dropna(subset=["job_title"])

    # Fill missing values
    df["seniority_level"] = df["seniority_level"].fillna("Unknown")
    df["status"] = df["status"].fillna("Unknown")
    df["location"] = df["location"].fillna("Unknown")
    df["ownership"] = df["ownership"].fillna("Unknown")
    df["revenue"] = df["revenue"].fillna("Unknown")

    # Standardize text
    df["job_title"] = df["job_title"].str.strip()
    df["company"] = df["company"].str.strip()

    print("\nAfter Cleaning:")
    print(df.shape)

    # Save cleaned file
    df.to_csv("../data/processed/jobs_clean.csv", index=False)

    print("\nCleaned dataset saved successfully!")