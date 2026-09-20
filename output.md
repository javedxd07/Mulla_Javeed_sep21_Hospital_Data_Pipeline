## 🖥️ Pipeline Execution Output

```text
========================================
STARTING HOSPITAL DATA PIPELINE
========================================
EXTRACT STEP
Patients extracted: 19 rows
Appointments extracted: 19 rows
Lab reports extracted: 18 rows
Wearable data extracted: 18 rows
Doctor notes extracted: 19 rows
----------------------------------------
TRANSFORM STEP
Patients after cleaning: 18 rows
Appointments after cleaning: 18 rows
Lab reports after cleaning: 18 rows
Wearable data after cleaning: 18 rows
Doctor notes after cleaning: 18 rows
----------------------------------------
Patients validation passed
Appointments validation passed
Lab reports validation passed
Wearable data validation passed
Doctor notes validation passed
----------------------------------------
Connection string loaded successfully
Host: localhost:3306/Hospitaldb
LOAD STEP
Loaded 18 rows into 'patients' table
Loaded 18 rows into 'appointments' table
Loaded 18 rows into 'lab_reports' table
Loaded 18 rows into 'wearable_data' table
Loaded 18 rows into 'doctor_notes' table
----------------------------------------
All data successfully loaded into MySQL!
========================================
PIPELINE COMPLETED SUCCESSFULLY
========================================
