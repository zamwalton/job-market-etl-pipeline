import pandas as pd
from sqlalchemy import create_engine, text
from config import *
def load_data():
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    # Read cleaned data
    df = pd.read_csv("../data/processed/jobs_clean.csv")

    # Clear existing data from table
    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE jobs RESTART IDENTITY"))

    # Load fresh data
    df.to_sql(
        "jobs",
        engine,
        if_exists="append",
        index=False
    )

    print("Data Loaded Successfully! ")