"""
pipeline.py
-----------
This file controls the entire ETL process. Instead of running every file
manually, we run this one file and it executes:

    Extract -> Transform -> Validate -> Load

in the correct order, using the correct data at each step.
"""

from extract import extract
from transform import transform
from validate import validate
from load import load


def run_pipeline():
    print("=" * 40)
    print("STARTING HOSPITAL DATA PIPELINE")
    print("=" * 40)

    # Step 1: Get the raw data from the CSV files.
    raw_data = extract()

    # Step 2: Clean and fix the raw data.
    clean_data = transform(raw_data)

    # Step 3: Double-check the cleaned data is actually correct.
    validate(clean_data)

    # Step 4: Store the cleaned, checked data into MySQL.
    load(clean_data)

    print("=" * 40)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 40)


if __name__ == "__main__":
    run_pipeline()
