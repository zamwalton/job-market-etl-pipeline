-- Create jobs table
CREATE TABLE IF NOT EXISTS jobs (
    job_title VARCHAR(255),
    seniority_level VARCHAR(100),
    status VARCHAR(100),
    company VARCHAR(255),
    location VARCHAR(255),
    post_date DATE,
    headquarter VARCHAR(255),
    industry VARCHAR(255),
    ownership VARCHAR(255),
    company_size VARCHAR(100),
    revenue VARCHAR(255),
    salary VARCHAR(255),
    skills TEXT
);