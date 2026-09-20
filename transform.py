"""
transform.py
------------
Transform means cleaning and changing the raw data into a format that is
easier and safer to use.

Raw data almost always has small problems - missing values, inconsistent
spelling, wrong data types, duplicate rows, and so on. If we send this
messy data straight into MySQL, our future SQL queries (and any future
Machine Learning model) could give wrong answers. So before loading the
data, we fix these problems here.

"""

import pandas as pd


def _parse_date_column(series):
    known_formats = ["%Y-%m-%d", "%d-%m-%Y"]
    result = pd.Series(pd.NaT, index=series.index, dtype="datetime64[ns]")

    for fmt in known_formats:
        still_missing = result.isna()
        parsed = pd.to_datetime(series[still_missing], format=fmt, errors="coerce")
        result.loc[still_missing] = parsed

    return result


def transform(raw_data):
    patients = _transform_patients(raw_data["patients"])
    appointments = _transform_appointments(raw_data["appointments"])
    lab_reports = _transform_lab_reports(raw_data["lab_reports"])
    wearable_data = _transform_wearable_data(raw_data["wearable_data"])
    doctor_notes = _transform_doctor_notes(raw_data["doctor_notes"])

    print("TRANSFORM STEP")
    print(f"Patients after cleaning: {len(patients)} rows")
    print(f"Appointments after cleaning: {len(appointments)} rows")
    print(f"Lab reports after cleaning: {len(lab_reports)} rows")
    print(f"Wearable data after cleaning: {len(wearable_data)} rows")
    print(f"Doctor notes after cleaning: {len(doctor_notes)} rows")
    print("-" * 40)

    return {
        "patients": patients,
        "appointments": appointments,
        "lab_reports": lab_reports,
        "wearable_data": wearable_data,
        "doctor_notes": doctor_notes,
    }


def _transform_patients(df):
    df = df.copy()

    # Problem: There is an exact duplicate patient row (same patient appears twice).
    # What we do: Drop duplicate rows.
    # Why: A duplicate patient would make our patient count and analytics wrong
    #      (it would look like we have more patients than we really do).
    df = df.drop_duplicates()

    # Problem: Gender is written inconsistently ("M", "Male", "male", "F", "Female", "female").
    # What we do: Convert everything to just two clean labels: "Male" and "Female".
    # Why: If "Male" and "M" are treated as different categories, any grouping or
    #      counting by gender (e.g. "how many male patients") will be wrong.
    gender_map = {
        "m": "Male", "male": "Male",
        "f": "Female", "female": "Female",
    }
    df["gender"] = df["gender"].astype(str).str.strip().str.lower().map(gender_map)

    # Problem: A couple of patients don't have an age recorded.
    # What we do: Fill the missing age using the median (middle) age of all patients.
    # Why: Leaving it blank could break later steps (like calculating average age),
    #      and using the median is a simple, safe guess that won't skew the data
    #      as much as picking a random number would.
    median_age = df["age"].median()
    df["age"] = df["age"].fillna(median_age)
    df["age"] = df["age"].astype(int)

    # Problem: Registration dates are written in two different formats
    # (e.g. "2023-01-15" and "15-01-2023").
    # What we do: Convert the whole column into one real pandas "date" type.
    # Why: SQL and Python can only sort, filter, or compare dates correctly if
    #      they are all stored in the same, real date format - not as plain text.
    # We use our _parse_date_column() helper here because this column mixes
    # two different date styles ("2023-01-15" and "15-01-2023"). It checks
    # each known format in turn so every row is read correctly, instead of
    # pandas guessing one format for the whole column.
    df["registration_date"] = _parse_date_column(df["registration_date"])

    df["phone"] = df["phone"].astype(str).str.strip()

    return df


def _transform_appointments(df):
    df = df.copy()

    # Problem: One appointment row is an exact duplicate.
    # What we do: Drop duplicate rows.
    # Why: A duplicate appointment would make it look like a patient visited
    #      twice when they only visited once, which would mess up counts.
    df = df.drop_duplicates()

    # Problem: A few appointments don't have a status filled in.
    # What we do: Fill missing status with "Unknown".
    # Why: We don't want to guess whether the appointment was completed or
    #      cancelled, so we clearly label it as "Unknown" instead of leaving
    #      it blank (a blank value can cause errors in SQL and reports).
    df["status"] = df["status"].fillna("Unknown")
    df["status"] = df["status"].replace("", "Unknown")

    # Problem: Appointment dates are stored as plain text.
    # What we do: Convert to a real date type.
    # Why: Same reason as before - real dates let us sort and filter properly.
    df["appointment_date"] = pd.to_datetime(df["appointment_date"], errors="coerce")

    return df


def _transform_lab_reports(df):
    df = df.copy()

    # Problem: Some test values are missing, and one is the text "pending"
    # instead of an actual number.
    # What we do: Convert the column to numbers, turning anything that isn't
    #      a valid number (like "pending") into a missing value, then fill
    #      missing values with the median test value for that same test.
    # Why: A lab value needs to be a number so we can do math on it later
    #      (averages, comparisons, risk checks). Grouping the median by
    #      test name is more accurate than using one single median for
    #      every different test (Blood Sugar and Cholesterol have very
    #      different normal ranges).
    df["test_value"] = pd.to_numeric(df["test_value"], errors="coerce")
    df["test_value"] = df.groupby("test_name")["test_value"].transform(
        lambda x: x.fillna(x.median())
    )

    # Problem: Test dates are stored as plain text.
    # What we do: Convert to a real date type.
    # Why: Needed for correct sorting/filtering, same as other date columns.
    df["test_date"] = pd.to_datetime(df["test_date"], errors="coerce")

    return df


def _transform_wearable_data(df):
    df = df.copy()

    df["heart_rate"] = pd.to_numeric(df["heart_rate"], errors="coerce")
    df["steps"] = pd.to_numeric(df["steps"], errors="coerce")
    df.loc[df["steps"] < 0, "steps"] = pd.NA
    df["steps"] = pd.to_numeric(df["steps"], errors="coerce")

    df["heart_rate"] = df["heart_rate"].fillna(df["heart_rate"].median())
    df["steps"] = df["steps"].fillna(df["steps"].median())
    df["heart_rate"] = df["heart_rate"].astype(int)
    df["steps"] = df["steps"].astype(int)


    df["sleep_hours"] = pd.to_numeric(df["sleep_hours"], errors="coerce")
    df["sleep_hours"] = df["sleep_hours"].fillna(df["sleep_hours"].median())

    df["record_date"] = pd.to_datetime(df["record_date"], errors="coerce")

    return df


def _transform_doctor_notes(df):
    df = df.copy()

    df = df.drop_duplicates()

    df["diagnosis"] = df["diagnosis"].fillna("Not specified")
    df["notes"] = df["notes"].fillna("No additional notes")

    df["visit_date"] = pd.to_datetime(df["visit_date"], errors="coerce")

    return df


if __name__ == "__main__":
    from extract import extract
    raw = extract()
    transform(raw)
