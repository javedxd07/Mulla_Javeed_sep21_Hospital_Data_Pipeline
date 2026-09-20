# 🏥 Hospital Patient Care Analytics Pipeline

> **A beginner-friendly Data Engineering project that transforms raw hospital data into clean, validated, and analytics-ready data using Python, Pandas, SQL, and MySQL.**

---

## 📌 Project Overview

Hospitals generate data from many different sources such as patient registration, appointments, laboratory systems, wearable devices, and doctor consultations.

The problem is that this data is usually stored separately and may contain **missing values, duplicates, inconsistent formats, and incorrect data**.

This project solves that problem by building a simple **ETL (Extract, Transform, Load) pipeline**.

The pipeline:

**Extracts** raw hospital data from CSV files →
**Transforms** and cleans the data →
**Validates** the cleaned data →
**Loads** it into MySQL →
**Analyzes** the data using SQL.

The final database contains five clean and structured tables that can be used for hospital analytics and can later support Machine Learning applications.

---

## 🎯 Project Objectives

The main objectives of this project are to:

* Collect hospital data from multiple sources
* Clean and standardize raw data
* Handle missing values and duplicate records
* Validate data before storing it
* Store cleaned data in MySQL
* Perform basic analytics using SQL
* Prepare the data for future high-risk patient prediction

---

## 🏥 Hospital Data Sources

The pipeline works with five different hospital data sources:

| Data Source             | CSV File            | MySQL Table     |
| ----------------------- | ------------------- | --------------- |
| 👤 Patient Registration | `patients.csv`      | `patients`      |
| 📅 Appointment System   | `appointments.csv`  | `appointments`  |
| 🧪 Laboratory System    | `lab_reports.csv`   | `lab_reports`   |
| ❤️ Wearable Devices     | `wearable_data.csv` | `wearable_data` |
| 🩺 Doctor Consultation  | `doctor_notes.csv`  | `doctor_notes`  |

---

## 🔄 ETL Pipeline

```text
                RAW HOSPITAL DATA
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
      Patients    Appointments    Labs
          │            │            │
          └────────────┼────────────┘
                       │
                 CSV FILES
                       │
                       ↓
                 📥 EXTRACT
                       │
                       ↓
                 🧹 TRANSFORM
              Clean & Standardize
                       │
                       ↓
                 ✅ VALIDATE
                Quality Checks
                       │
                       ↓
                 🗄️ LOAD
                  MySQL
                       │
                       ↓
                 📊 SQL ANALYTICS
                       │
                       ↓
              Future ML / Prediction
```

### In simple words

**Extract:** Read the raw CSV files.

**Transform:** Clean missing values, duplicates, formats, and data types.

**Validate:** Check whether the cleaned data is valid.

**Load:** Store the final data in MySQL.

**Analyze:** Use SQL queries to understand the hospital data.

---

## 📂 Project Structure

```text
hospital_data_pipeline/
│
├── 📁 data/
│   ├── patients.csv
│   ├── appointments.csv
│   ├── lab_reports.csv
│   ├── wearable_data.csv
│   └── doctor_notes.csv
│
├── config.py
├── extract.py
├── transform.py
├── validate.py
├── load.py
├── pipeline.py
├── requirements.txt
├── .gitignore
└── README.md
```

### 🧩 What Each File Does

| File               | Purpose                                                   |
| ------------------ | --------------------------------------------------------- |
| `config.py`        | Stores MySQL database connection settings                 |
| `extract.py`       | Reads the five CSV files using Pandas                     |
| `transform.py`     | Cleans and standardizes the raw data                      |
| `validate.py`      | Checks the quality of the cleaned data                    |
| `load.py`          | Loads the validated data into MySQL                       |
| `pipeline.py`      | Runs the complete ETL process                             |
| `requirements.txt` | Contains required Python packages                         |
| `.gitignore`       | Prevents sensitive/unnecessary files from being committed |

---

## 🧹 Data Transformation

The raw datasets intentionally contain realistic data-quality problems.

The transformation stage handles problems such as:

* Missing values
* Duplicate records
* Inconsistent formats
* Incorrect data types
* Date formatting
* Numeric conversions
* Inconsistent categorical values

The goal is simple:

> **Raw data → Clean and consistent data**

---

## ✅ Data Validation

Before loading the data into MySQL, the pipeline performs quality checks.

Examples include:

* Patient IDs should not be empty
* Ages should not be negative
* Gender values should be valid
* Laboratory values should be numeric
* Heart rate should be within a reasonable range
* Steps should not be negative
* Dates should be valid
* Appointments should belong to valid patients

If the validation fails, the pipeline stops instead of loading potentially incorrect data.

---

## 🗄️ MySQL Database

After successful validation, the cleaned data is loaded into the **Hospitaldb** MySQL database.

### Database Tables

```text
Hospitaldb
│
├── patients
├── appointments
├── lab_reports
├── wearable_data
└── doctor_notes
```

These tables keep the different hospital data sources organized while allowing them to be connected using patient IDs.

---

## 💻 Running the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd hospital_data_pipeline
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create the MySQL database

```sql
CREATE DATABASE Hospitaldb;
```

### 4. Configure database credentials

Set your MySQL username, password, host, and database name in your configuration.

> **Important:** Do not upload your real database password to GitHub.

If you are using a `.env` file, make sure it is included in `.gitignore`.

### 5. Run the complete pipeline

```bash
python pipeline.py
```

This single command runs:

```text
Extract
   ↓
Transform
   ↓
Validate
   ↓
Load
```

---

## 🖥️ Expected Pipeline Output

A successful run should show output similar to:

```text
========================================
        HOSPITAL DATA PIPELINE
========================================

EXTRACT STEP
Loaded patients.csv
Loaded appointments.csv
Loaded lab_reports.csv
Loaded wearable_data.csv
Loaded doctor_notes.csv

TRANSFORM STEP
Cleaning patient data...
Cleaning appointment data...
Cleaning laboratory data...
Cleaning wearable data...
Cleaning doctor notes...

VALIDATION STEP
All validation checks passed!

LOAD STEP
Loaded data into 'patients'
Loaded data into 'appointments'
Loaded data into 'lab_reports'
Loaded data into 'wearable_data'
Loaded data into 'doctor_notes'

----------------------------------------
All data successfully loaded into MySQL!
----------------------------------------
```

---

## 📸 Project Output

### Pipeline Execution

*Add your terminal screenshot here.*

```text
📷 Screenshot:
ETL pipeline successfully executed
```

### MySQL Database

*Add your MySQL screenshot here.*

```text
📷 Screenshot:
Hospitaldb → SHOW TABLES;
```

Expected tables:

```text
patients
appointments
lab_reports
wearable_data
doctor_notes
```

### Sample Table Data

*Add screenshots of your MySQL table results here.*

Recommended screenshots:

* `SELECT * FROM patients;`
* `SELECT * FROM appointments;`
* `SELECT * FROM lab_reports;`
* `SELECT * FROM wearable_data;`
* `SELECT * FROM doctor_notes;`

---

## 📊 SQL Analytics

Once the data is loaded into MySQL, we can perform basic analytics.

### 1. Total Patients

```sql
SELECT COUNT(*) AS total_patients
FROM patients;
```

### 2. Total Appointments

```sql
SELECT COUNT(*) AS total_appointments
FROM appointments;
```

### 3. Appointments by Department

```sql
SELECT department, COUNT(*) AS appointment_count
FROM appointments
GROUP BY department
ORDER BY appointment_count DESC;
```

### 4. Average Patient Age

```sql
SELECT AVG(age) AS average_age
FROM patients;
```

### 5. Average Heart Rate

```sql
SELECT AVG(heart_rate) AS average_heart_rate
FROM wearable_data;
```

### 6. Total Laboratory Tests

```sql
SELECT COUNT(*) AS total_lab_tests
FROM lab_reports;
```

### 7. Patient Appointment History

```sql
SELECT *
FROM appointments
WHERE patient_id = 'P001'
ORDER BY appointment_date;
```

### 8. Patients and Their Lab Results

```sql
SELECT
    p.patient_id,
    p.name,
    l.test_name,
    l.test_value,
    l.test_date
FROM patients p
JOIN lab_reports l
    ON p.patient_id = l.patient_id
ORDER BY p.patient_id;
```

### 9. Higher Heart Rate Readings

```sql
SELECT
    p.patient_id,
    p.name,
    w.heart_rate,
    w.record_date
FROM patients p
JOIN wearable_data w
    ON p.patient_id = w.patient_id
WHERE w.heart_rate > 85
ORDER BY w.heart_rate DESC;
```

### 10. Appointments by Status

```sql
SELECT status, COUNT(*) AS count
FROM appointments
GROUP BY status;
```

---

## 🔗 How This Maps to the Case Study

```text
Hospital Case Study
        │
        ├── Patient Registration
        │       ↓
        │   patients.csv
        │
        ├── Appointment Scheduling
        │       ↓
        │   appointments.csv
        │
        ├── Laboratory Reports
        │       ↓
        │   lab_reports.csv
        │
        ├── Wearable Health Devices
        │       ↓
        │   wearable_data.csv
        │
        └── Doctor Consultation
                ↓
            doctor_notes.csv
```

The pipeline brings all these sources together:

```text
Multiple Hospital Sources
          ↓
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

---

## 💡 What Does This Project Achieve?

This project demonstrates the complete basic Data Engineering workflow:

```text
Raw Data
   ↓
Data Cleaning
   ↓
Data Validation
   ↓
Data Storage
   ↓
Data Analytics
```

Instead of manually cleaning and moving data every time, the process can be executed with a single command:

```bash
python pipeline.py
```

This makes the process **repeatable, organized, and easier to maintain**.

---

## 🤖 Future Scope

The current project focuses on Data Engineering fundamentals.

Possible future improvements include:

* 📊 Building a hospital analytics dashboard
* 📈 Adding more advanced SQL analytics
* 🏥 Adding more hospital departments
* 🤖 Building a Machine Learning model for high-risk patient prediction
* 📅 Improving appointment scheduling analytics
* 🔄 Automating the data pipeline
* 📱 Creating a web interface for hospital analytics

### Data Engineering → Machine Learning

```text
Data Sources
     ↓
Data Engineering
     ↓
Clean & Validated Data
     ↓
Feature Preparation
     ↓
Machine Learning
     ↓
Risk Prediction
```

> **Data Engineering prepares the data. Machine Learning can use that prepared data later.**

---

## 🛠️ Technologies Used

| Technology    | Purpose                 |
| ------------- | ----------------------- |
| 🐍 Python     | Pipeline development    |
| 🐼 Pandas     | Data processing         |
| 🗄️ MySQL     | Data storage            |
| 🔍 SQL        | Data analysis           |
| 🔗 SQLAlchemy | Python–MySQL connection |
| 📄 CSV        | Raw data source         |

---

## 🔐 Data Privacy

All datasets used in this project contain **fictional data only**.

No real patient information is used.

The datasets intentionally contain a few data-quality issues so that the transformation and validation stages can demonstrate how an ETL pipeline handles imperfect raw data.

---

## 🎓 Key Learning Outcomes

Through this project, I practiced:

* Understanding ETL
* Working with multiple datasets
* Reading CSV files using Pandas
* Cleaning raw data
* Handling missing values
* Removing duplicate records
* Validating data quality
* Connecting Python with MySQL
* Loading data into database tables
* Writing SQL queries
* Using SQL JOINs
* Designing a simple Data Engineering pipeline

---

## 👨‍💻 Project Summary

**Hospital Patient Care Analytics Pipeline** is a beginner-level Data Engineering project that demonstrates how data from multiple hospital sources can be collected, cleaned, validated, stored, and analyzed.

The project focuses on building a strong foundation in **ETL, Python, Pandas, SQL, and MySQL** without adding unnecessary complexity.

---

### ⭐ Project Flow

```text
        🏥 HOSPITAL DATA
              │
              ↓
        📥 EXTRACT
              │
              ↓
        🧹 TRANSFORM
              │
              ↓
        ✅ VALIDATE
              │
              ↓
        🗄️ MYSQL DATABASE
              │
              ↓
        📊 SQL ANALYTICS
              │
              ↓
        🤖 FUTURE ML
```

**Built as a Data Engineering fundamentals project.**
