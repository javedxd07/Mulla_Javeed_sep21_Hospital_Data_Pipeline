# Hospital Patient Care Analytics Pipeline

A simple, beginner-friendly Data Engineering project that collects hospital data
from five sources, cleans it, checks it, and stores it in MySQL so it's ready
for SQL analytics (and, later, Machine Learning).

---

## 1. What did I build?

I built a simple ETL (Extract, Transform, Load) pipeline for a hospital that
collects data from five different sources: patient registration, appointments,
lab reports, wearable devices, and doctor notes. The pipeline reads this raw
data from CSV files, cleans up problems like missing values and duplicates,
checks that the cleaned data is correct, and then stores it into a MySQL
database as separate tables. Once the data is in MySQL, it can be explored
using simple SQL queries, and it's also in a good shape to be used by a
Machine Learning model in the future.

## 2. Why did I use ETL?

Hospital data comes from many different places, and raw data is almost never
clean - it has missing values, duplicates, and inconsistent formatting. ETL
gives us a simple, repeatable three-step process to deal with this: **Extract**
the data from its source, **Transform** (clean) it so it's consistent and
usable, and **Load** it into a proper database. Doing this step by step, in
separate files, makes the project easy to understand, test, and reuse.

---

## 3. Project structure

```text
hospital_data_pipeline/
│
├── data/
│   ├── patients.csv
│   ├── appointments.csv
│   ├── lab_reports.csv
│   ├── wearable_data.csv
│   └── doctor_notes.csv
│
├── config.py       -> database connection settings
├── extract.py       -> reads the CSV files
├── transform.py     -> cleans the data
├── validate.py      -> checks the cleaned data
├── load.py           -> stores data in MySQL
├── pipeline.py       -> runs everything in order
├── requirements.txt
└── README.md
```

### What each file does

| File         | What it does |
|--------------|---------------|
| `config.py`   | Stores the MySQL database settings (user, password, host, database name) |
| `extract.py`  | Gets the raw data from the five CSV files into pandas |
| `transform.py`| Cleans the data (fixes missing values, duplicates, formats, data types) |
| `validate.py` | Does a final quality check on the cleaned data before loading it |
| `load.py`     | Stores the cleaned, checked data into MySQL tables |
| `pipeline.py` | Runs Extract → Transform → Validate → Load, in order, with one command |

---

## 4. What happens when I run `pipeline.py`?

1. **Extract** - the pipeline opens the five CSV files and loads them into
   pandas DataFrames (basically, tables inside Python). It prints how many
   rows came from each file.
2. **Transform** - each dataset is cleaned individually: duplicates are
   removed, missing values are filled sensibly, gender/date formats are made
   consistent, and text columns are converted to proper numbers or dates
   where needed.
3. **Validate** - the cleaned data goes through a set of checks (for example,
   "no negative ages", "no unrealistic heart rates", "every appointment
   belongs to a real patient"). If anything fails, the pipeline stops with a
   clear error instead of silently loading bad data.
4. **Load** - once validation passes, each cleaned table is written into
   MySQL using SQLAlchemy and pandas' `to_sql()`, creating five tables:
   `patients`, `appointments`, `lab_reports`, `wearable_data`, `doctor_notes`.

You'll see clear step-by-step print statements in the terminal the whole way
through, so it's easy to follow what the pipeline is doing.

---

## 5. Installation and execution

### Install the required Python packages

```bash
pip install -r requirements.txt
```

### Set up MySQL

Open MySQL and create the database:

```sql
CREATE DATABASE hospital_db;
```

**In simple English:** this command tells MySQL "create a new, empty
container called `hospital_db` where all our hospital tables will live."
Everything the pipeline loads later goes inside this container.

### Set your database credentials (recommended, instead of hardcoding them)

```bash
export HOSPITAL_DB_USER=root
export HOSPITAL_DB_PASSWORD=your_actual_password
export HOSPITAL_DB_HOST=localhost
export HOSPITAL_DB_NAME=hospital_db
```

(On Windows PowerShell, use `$env:HOSPITAL_DB_USER = "root"` and so on.)

### Run the pipeline

```bash
python pipeline.py
```

This single command runs Extract → Transform → Validate → Load, and your
MySQL database will end up with five clean, ready-to-query tables.

---

## 6. Checking the data in MySQL

```sql
SELECT * FROM patients;
SELECT * FROM appointments;
SELECT * FROM lab_reports;
SELECT * FROM wearable_data;
SELECT * FROM doctor_notes;
```

These simply show you every row in each table, so you can visually confirm
the pipeline loaded the data correctly.

---

## 7. Simple analytics SQL queries

**1. Total number of patients**
```sql
SELECT COUNT(*) AS total_patients FROM patients;
```
Counts how many patient rows exist - a quick headline number for the hospital.

**2. Total appointments**
```sql
SELECT COUNT(*) AS total_appointments FROM appointments;
```
Counts how many appointments have been booked in total.

**3. Appointments by department**
```sql
SELECT department, COUNT(*) AS appointment_count
FROM appointments
GROUP BY department
ORDER BY appointment_count DESC;
```
Groups appointments by department so we can see which departments are
busiest.

**4. Average patient age**
```sql
SELECT AVG(age) AS average_age FROM patients;
```
Calculates the average age across all patients, useful for understanding who
the hospital mostly treats.

**5. Average heart rate from wearables**
```sql
SELECT AVG(heart_rate) AS average_heart_rate FROM wearable_data;
```
Gives the average heart rate recorded across all wearable device readings.

**6. Number of lab tests performed**
```sql
SELECT COUNT(*) AS total_lab_tests FROM lab_reports;
```
Counts how many lab tests have been recorded in total.

**7. Appointment history for one patient**
```sql
SELECT *
FROM appointments
WHERE patient_id = 'P001'
ORDER BY appointment_date;
```
Shows every appointment for a specific patient, in date order - useful for
seeing a patient's visit history at a glance.

**8. Patients with their lab results (JOIN)**
```sql
SELECT p.patient_id, p.name, l.test_name, l.test_value, l.test_date
FROM patients p
JOIN lab_reports l ON p.patient_id = l.patient_id
ORDER BY p.patient_id;
```
Joins the patients table with the lab_reports table so each lab result is
shown together with the patient's name, instead of just a patient ID.

**9. Patients with unusually high heart rate**
```sql
SELECT p.patient_id, p.name, w.heart_rate, w.record_date
FROM patients p
JOIN wearable_data w ON p.patient_id = w.patient_id
WHERE w.heart_rate > 85
ORDER BY w.heart_rate DESC;
```
Finds patients whose wearable device recorded a higher-than-normal heart
rate - a simple example of the kind of check that could later feed into
high-risk patient prediction.

**10. Number of appointments per status**
```sql
SELECT status, COUNT(*) AS count
FROM appointments
GROUP BY status;
```
Shows how many appointments were Completed, Cancelled, Scheduled, or Unknown
- useful for tracking how well the hospital keeps up with its schedule.

---

## 8. How this matches the hospital case study

```text
Patient Registration  -> patients.csv
Appointment System     -> appointments.csv
Laboratory System      -> lab_reports.csv
Wearable Devices        -> wearable_data.csv
Doctor Consultation      -> doctor_notes.csv
```

```text
CSV Files
   ↓
Extract
   ↓
Transform
   ↓
Validate
   ↓
MySQL
   ↓
SQL Analytics
```

**In simple English:** the hospital has data spread across different
systems - registration, appointments, lab, wearables, and doctor notes. Our
pipeline brings all of this data together, cleans it, checks it, and stores
it in one place (MySQL). Once the data is organized like this, the hospital
can use simple SQL queries to understand things like how busy each
department is, what the average patient looks like, and which patients might
need closer attention.

## 9. How does this solve the hospital case study?

The case study asked for a simple end-to-end system that can collect,
clean, validate, store, and prepare hospital data for analytics and future
risk prediction - and that's exactly what this project does, using only
beginner-friendly tools (Python, pandas, SQL, MySQL, SQLAlchemy), without any
unnecessary complexity like cloud services or Machine Learning frameworks.

## 10. Future high-risk patient prediction

This project does **not** build a Machine Learning model. What it does is
prepare clean, structured, and validated patient data - which is exactly
what a Machine Learning model would need as a starting point. In the future,
this same MySQL data (age, heart rate, lab values, appointment history, and
so on) could be given to an ML model trained to spot patients who might be
at higher risk, so doctors can check on them sooner. In short: **Data
Engineering prepares the data, and Machine Learning would use that prepared
data later.**

## 11. What can be added later?

- Collecting data from more hospital departments
- More advanced analytics and reports
- A dashboard to visualize the data (e.g. Power BI or a simple web page)
- A Machine Learning model to predict high-risk patients
- Automated appointment scheduling based on doctor availability

---

## 12. Notes on the data

Every CSV in this project uses **fictional data only** - no real patient
information. Each file also intentionally includes a few realistic problems
(a missing value, a duplicate row, an inconsistent format) so that the
`transform.py` and `validate.py` steps have something real to clean and
check - this mirrors what raw hospital data usually looks like in practice.
