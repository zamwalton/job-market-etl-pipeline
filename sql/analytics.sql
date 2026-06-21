/* Top 10 Job Titles */

SELECT job_title, COUNT(*) AS total_jobs
FROM jobs
GROUP BY job_title
ORDER BY total_jobs DESC
LIMIT 10;

/* Most Common Seniority Levels */

SELECT seniority_level, COUNT(*) AS total
FROM jobs
GROUP BY seniority_level
ORDER BY total DESC;

/* Top Hiring Locations */

SELECT location, COUNT(*) AS total_jobs
FROM jobs
GROUP BY location
ORDER BY total_jobs DESC
LIMIT 10;

/* Top Industries */

SELECT industry, COUNT(*) AS total_jobs
FROM jobs
GROUP BY industry
ORDER BY total_jobs DESC
LIMIT 10;

/* Companies Posting the Most Jobs*/

SELECT company, COUNT(*) AS total_jobs
FROM jobs
GROUP BY company
ORDER BY total_jobs DESC
LIMIT 10;


