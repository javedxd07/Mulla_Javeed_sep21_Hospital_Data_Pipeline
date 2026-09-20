"""
validate.py
-----------
Validation is like a final quality check. Before putting the data into
MySQL, we make sure the cleaned data is still correct.

Transform.py already fixed most problems, but validation is our safety
net - it double-checks that the cleaning actually worked and nothing
slipped through. We use simple pandas checks combined with "assert"
statements.

A quick note on "assert": an assert statement checks that something is
True. If it's True, nothing happens and the code just continues. If it's
False, Python stops immediately and shows an error - which is exactly
what we want, because it means bad data should NOT continue into MySQL.
"""


def validate(clean_data):
    _validate_patients(clean_data["patients"])
    _validate_appointments(clean_data["appointments"], clean_data["patients"])
    _validate_lab_reports(clean_data["lab_reports"])
    _validate_wearable_data(clean_data["wearable_data"])
    _validate_doctor_notes(clean_data["doctor_notes"])
    print("-" * 40)


def _validate_patients(df):
    # Patient ID should never be empty - it's how we identify each patient.
    assert df["patient_id"].notna().all(), "Some patient_id values are missing"

    # Age should never be negative - a negative age makes no real-world sense.
    assert (df["age"] >= 0).all(), "Found a negative age"

    # Gender should only ever be "Male" or "Female" after our cleaning step.
    assert df["gender"].isin(["Male", "Female"]).all(), "Found an unexpected gender value"

    # Registration date should be a real, valid date for every patient.
    assert df["registration_date"].notna().all(), "Some registration dates are invalid"

    print("Patients validation passed")


def _validate_appointments(df, patients_df):
    # Every appointment must be linked to a patient_id that actually exists
    # in our patients table - otherwise it's an appointment for "no one".
    valid_patient_ids = set(patients_df["patient_id"])
    assert df["patient_id"].isin(valid_patient_ids).all(), "Found an appointment with an unknown patient_id"

    # Appointment date should be a valid date.
    assert df["appointment_date"].notna().all(), "Some appointment dates are invalid"

    print("Appointments validation passed")


def _validate_lab_reports(df):
    # Test value must be numeric (transform.py already converts it, so this
    # check confirms there are no leftover missing values).
    assert df["test_value"].notna().all(), "Some lab test values are still missing"

    # Test date should be valid.
    assert df["test_date"].notna().all(), "Some lab test dates are invalid"

    print("Lab reports validation passed")


def _validate_wearable_data(df):
    # Heart rate should be within a realistic human range.
    # (Below 30 or above 220 would almost certainly be a device error, not a real reading.)
    assert df["heart_rate"].between(30, 220).all(), "Found an unrealistic heart rate"

    # Steps should never be negative.
    assert (df["steps"] >= 0).all(), "Found negative steps"

    # Record date should be valid.
    assert df["record_date"].notna().all(), "Some wearable record dates are invalid"

    print("Wearable data validation passed")


def _validate_doctor_notes(df):
    # Visit date should be valid.
    assert df["visit_date"].notna().all(), "Some doctor note visit dates are invalid"

    # Diagnosis should never be truly empty - it should at least say "Not specified".
    assert df["diagnosis"].notna().all(), "Some diagnosis fields are missing"

    print("Doctor notes validation passed")


if __name__ == "__main__":
    from extract import extract
    from transform import transform

    raw = extract()
    clean = transform(raw)
    validate(clean)
