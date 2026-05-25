CREATE DATABASE healthcare_analysis;

USE healthcare_analysis;

CREATE TABLE appointments (
    PatientId BIGINT,
    AppointmentID BIGINT,
    Gender VARCHAR(10),
    ScheduledDay DATETIME,
    AppointmentDay DATETIME,
    Age INT,
    Neighbourhood VARCHAR(100),
    Scholarship INT,
    Hipertension INT,
    Diabetes INT,
    Alcoholism INT,
    Handcap INT,
    SMS_received INT,
    No_show VARCHAR(10)
);

SELECT * FROM appointments;

-- Total Appointments
SELECT COUNT(*) AS total_appointments
FROM appointments;

-- No-show Rate
SELECT
    COUNT(CASE WHEN No_show='Yes' THEN 1 END)*100.0/COUNT(*) AS no_show_rate
FROM appointments;

-- Appointment Completion Rate
SELECT
    COUNT(CASE WHEN No_show='No' THEN 1 END)*100.0/COUNT(*) AS completion_rate
FROM appointments;

-- Gender-wise Appointments
SELECT Gender,
       COUNT(*) AS total
FROM appointments
GROUP BY Gender;

-- Average Age
SELECT AVG(Age) AS avg_age
FROM appointments;

-- SMS Reminder Analysis
SELECT SMS_received,
       COUNT(*) AS total_patients
FROM appointments
GROUP BY SMS_received;

-- Age Group Analysis
SELECT
    CASE
        WHEN Age < 18 THEN 'Children'
        WHEN Age BETWEEN 18 AND 40 THEN 'Adults'
        WHEN Age BETWEEN 41 AND 60 THEN 'Middle Age'
        ELSE 'Senior Citizens'
    END AS age_group,
    COUNT(*) AS total_patients
FROM appointments
GROUP BY age_group;

-- Top Neighbourhoods with No-show
SELECT Neighbourhood,
       COUNT(*) AS no_show_count
FROM appointments
WHERE No_show='Yes'
GROUP BY Neighbourhood
ORDER BY no_show_count DESC
LIMIT 10;