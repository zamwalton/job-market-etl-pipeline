# Job Market ETL Pipeline

## Project Overview

This project is a beginner-friendly Data Engineering project that demonstrates the complete ETL (Extract, Transform, Load) process using Python, Pandas, and PostgreSQL.

The pipeline extracts job market data from a CSV dataset, performs data profiling and cleaning, and loads the processed data into a PostgreSQL database for analysis and reporting.

---

## Objectives

- Extract data from a CSV dataset
- Profile data to identify quality issues
- Clean and transform the dataset
- Load data into PostgreSQL
- Create SQL views for analysis
- Execute business intelligence queries
- Build a reusable ETL pipeline

---

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- Psycopg2
- SQL

---

## Dataset

Dataset: Data Science Job Postings with Salaries (2025)

Columns:

- job_title
- seniority_level
- status
- company
- location
- post_date
- headquarter
- industry
- ownership
- company_size
- revenue
- salary
- skills

---

## Project Structure

```text
job-market-pipeline/
│
├── data/
│   ├── raw/
│   │   └── jobs.csv
│   │
│   └── processed/
│       └── jobs_clean.csv
│
├── scripts/
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── data_quality.py
│   └── main.py
│
├── sql/
│   ├── setup.sql
│   ├── create_view.sql
│   └── analytics.sql
│
├── pipeline.log
├── requirements.txt
└── README.md
```

---

## ETL Workflow

### 1. Extract

Read the raw dataset using Pandas.

```python
df = pd.read_csv("../data/raw/jobs.csv")
```

### 2. Profile

Analyze:

- Missing values
- Duplicate rows
- Data types
- Dataset statistics

### 3. Transform

Data cleaning performed:

- Removed rows with missing job titles
- Filled missing values
- Standardized text fields
- Generated cleaned dataset

Output:

```text
data/processed/jobs_clean.csv
```

### 4. Load

Load cleaned data into PostgreSQL.

Pipeline process:

```text
CSV Dataset
    ↓
Extract
    ↓
Profile
    ↓
Transform
    ↓
PostgreSQL
```

---

## Database

Database:

```text
job_pipeline
```

Table:

```text
jobs
```

View:

```sql
CREATE OR REPLACE VIEW job_summary AS
SELECT
    job_title,
    seniority_level,
    location,
    industry,
    salary
FROM jobs;
```

---

## Running the Pipeline

Navigate to the scripts directory:

```bash
cd scripts
```

Run the complete pipeline:

```bash
python main.py
```

Expected output:

```text
Pipeline Completed Successfully!
```

---

## Data Quality Checks

The pipeline validates:

- Missing values
- Duplicate records
- Dataset consistency

Example:

```python
print(df.isnull().sum())
print(df.duplicated().sum())
```

---

## Sample SQL Analytics

### Top Job Titles

```sql
SELECT job_title, COUNT(*) AS total_jobs
FROM jobs
GROUP BY job_title
ORDER BY total_jobs DESC
LIMIT 10;
```

### Top Hiring Locations

```sql
SELECT location, COUNT(*) AS total_jobs
FROM jobs
GROUP BY location
ORDER BY total_jobs DESC
LIMIT 10;
```

### Most Common Seniority Levels

```sql
SELECT seniority_level, COUNT(*) AS total_jobs
FROM jobs
GROUP BY seniority_level
ORDER BY total_jobs DESC;
```

### Top Industries

```sql
SELECT industry, COUNT(*) AS total_jobs
FROM jobs
GROUP BY industry
ORDER BY total_jobs DESC
LIMIT 10;
```

---

## Challenges Solved

### PostgreSQL View Dependency Error

Issue:

```text
cannot drop table jobs because other objects depend on it
```

Cause:

- job_summary view depended on jobs table
- Pandas was using if_exists='replace'

Solution:

```sql
TRUNCATE TABLE jobs RESTART IDENTITY;
```

Followed by:

```python
if_exists="append"
```

This preserved database objects while preventing duplicate data.

---

## Key Skills Demonstrated

- ETL Pipeline Development
- Data Cleaning and Transformation
- Data Profiling
- PostgreSQL Database Management
- SQL Query Writing
- Configuration Management
- Logging
- Pipeline Automation
- Data Quality Validation

---

## Future Enhancements

- Power BI Dashboard
- Apache Airflow Scheduling
- Data Warehouse Design
- Star Schema Modeling
- Automated Data Validation
- Docker Deployment

---

## Author

Developed as a Data Engineering learning project to gain hands-on experience with ETL pipelines, SQL, and PostgreSQL.