/* Create a Reporting View */

CREATE VIEW job_summary AS
SELECT
    job_title,
    seniority_level,
    location,
    industry,
    salary
FROM jobs;

/* Display the view */

SELECT * FROM job_summary;