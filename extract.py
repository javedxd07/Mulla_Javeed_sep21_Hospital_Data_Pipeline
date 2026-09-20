
import pandas as pd

DATA_FOLDER = "data"


def extract():
    """
    Reads all five hospital CSV files using pandas and returns them
    together in a dictionary, so the rest of the pipeline can access
    each dataset by name (like raw_data["patients"]).
    """

    patients = pd.read_csv(f"{DATA_FOLDER}/patients.csv")
    appointments = pd.read_csv(f"{DATA_FOLDER}/appointments.csv")
    lab_reports = pd.read_csv(f"{DATA_FOLDER}/lab_reports.csv")
    wearable_data = pd.read_csv(f"{DATA_FOLDER}/wearable_data.csv")
    doctor_notes = pd.read_csv(f"{DATA_FOLDER}/doctor_notes.csv")

    # We print row counts here just so we can see, at a glance, that the
    # data actually loaded and roughly how big each dataset is.
    print("EXTRACT STEP")
    print(f"Patients extracted: {len(patients)} rows")
    print(f"Appointments extracted: {len(appointments)} rows")
    print(f"Lab reports extracted: {len(lab_reports)} rows")
    print(f"Wearable data extracted: {len(wearable_data)} rows")
    print(f"Doctor notes extracted: {len(doctor_notes)} rows")
    print("-" * 40)

    return {
        "patients": patients,
        "appointments": appointments,
        "lab_reports": lab_reports,
        "wearable_data": wearable_data,
        "doctor_notes": doctor_notes,
    }


if __name__ == "__main__":
    # This lets us test extract.py on its own, without running the whole
    # pipeline, just to make sure the files load correctly.
    extract()
