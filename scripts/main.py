from datetime import datetime
from extract import extract_data
from transform import transform_data
from load import load_data

extract_data()
transform_data()
load_data()

with open("../pipeline.log", "a") as log:
    log.write(
        f"{datetime.now()} - Pipeline completed successfully\n"
    )

print("Pipeline Completed Successfully!")