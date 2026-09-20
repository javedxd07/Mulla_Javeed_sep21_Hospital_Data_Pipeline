"""
load.py
-------
Load means taking the cleaned and checked data from Python and storing it
inside MySQL.

This is the last step of ETL (Extract, Transform, Load). Once the data is
sitting safely in MySQL as proper tables, anyone (us, an analyst, or later
a Machine Learning model) can query it using plain SQL, without needing to
run any Python code.

"""

from sqlalchemy import create_engine
from config import CONNECTION_STRING


def load(clean_data):
    print("Connection string loaded successfully")
    print("Host:", CONNECTION_STRING.split("@")[-1])

    engine = create_engine(CONNECTION_STRING)
    
    table_names = {
        "patients": "patients",
        "appointments": "appointments",
        "lab_reports": "lab_reports",
        "wearable_data": "wearable_data",
        "doctor_notes": "doctor_notes",
    }

    print("LOAD STEP")
    for key, table_name in table_names.items():
        df = clean_data[key]

        # if_exists="replace" means: if the table already exists, drop it
        # and recreate it fresh with today's cleaned data. This keeps things
        # simple for a beginner project - every time we run the pipeline,
        # MySQL gets an up-to-date copy of the cleaned data.
        df.to_sql(table_name, con=engine, if_exists="replace", index=False)
        print(f"Loaded {len(df)} rows into '{table_name}' table")

    print("-" * 40)
    print("All data successfully loaded into MySQL!")


if __name__ == "__main__":
    from extract import extract
    from transform import transform
    from validate import validate

    raw = extract()
    clean = transform(raw)
    validate(clean)
    load(clean)
