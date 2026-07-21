/*=============================================================================
  Government Information Analytics Platform - Snowflake Migration
  File: 05_load_raw_data.sql
  Purpose: Load weighted ministry CSV files into the raw reporting table.
  Author: Jonathan Mukundu
  Date: 2026-07-21

  Revision History:
  - 2026-07-20 | Jonathan Mukundu | Initial scaffold.
  - 2026-07-21 | Jonathan Mukundu | Implemented idempotent ministry CSV load.
=============================================================================*/

USE ROLE ACCOUNTADMIN;
USE WAREHOUSE GOV_MIS_WH;
USE DATABASE GOVERNMENT_MIS;

-- Snowflake load history prevents unchanged staged files from being loaded again.
-- PROGRAM_NAME ($5) and SUBMISSION_STATUS ($12) are intentionally omitted because
-- they are not columns in the existing RAW_MINISTRY_REPORTS table.
COPY INTO GOVERNMENT_MIS.RAW.RAW_MINISTRY_REPORTS (
    MINISTRY,
    SOURCE_FILE,
    REPORTING_PERIOD,
    PROVINCE,
    DISTRICT,
    PROGRAM_ID,
    INDICATOR_CODE,
    INDICATOR_NAME,
    REPORTED_VALUE,
    TARGET_VALUE,
    REPORTING_OFFICER,
    SUBMISSION_DATE,
    INGESTION_TIMESTAMP
)
FROM (
    SELECT
        $13::VARCHAR,
        SPLIT_PART(METADATA$FILENAME, '/', -1)::VARCHAR,
        $1::VARCHAR,
        $2::VARCHAR,
        $3::VARCHAR,
        $4::VARCHAR,
        $6::VARCHAR,
        $7::VARCHAR,
        $8::FLOAT,
        $9::FLOAT,
        $10::VARCHAR,
        $11::DATE,
        CURRENT_TIMESTAMP()::TIMESTAMP_NTZ
    FROM @GOVERNMENT_MIS.RAW.MINISTRY_REPORTS_STAGE
)
FILES = (
    'MCTI_WEIGHTED_2025_2026.csv',
    'MGEE_WEIGHTED_2025_2026.csv'
)
FILE_FORMAT = (FORMAT_NAME = GOVERNMENT_MIS.RAW.MINISTRY_REPORTS_CSV_FORMAT)
ON_ERROR = 'ABORT_STATEMENT'
FORCE = FALSE;

-- The COPY INTO result returned above reports each file's load status and row count.
SELECT
    FILE_NAME,
    STATUS,
    ROW_PARSED,
    ROW_COUNT,
    ERROR_COUNT,
    FIRST_ERROR_MESSAGE,
    LAST_LOAD_TIME
FROM TABLE(
    GOVERNMENT_MIS.INFORMATION_SCHEMA.COPY_HISTORY(
        TABLE_NAME => 'GOVERNMENT_MIS.RAW.RAW_MINISTRY_REPORTS',
        START_TIME => DATEADD('HOUR', -1, CURRENT_TIMESTAMP())
    )
)
ORDER BY LAST_LOAD_TIME DESC, FILE_NAME;

SELECT COUNT(*) AS TOTAL_LOADED_ROWS
FROM GOVERNMENT_MIS.RAW.RAW_MINISTRY_REPORTS;

SELECT
    MINISTRY,
    COUNT(*) AS LOADED_ROWS
FROM GOVERNMENT_MIS.RAW.RAW_MINISTRY_REPORTS
GROUP BY MINISTRY
ORDER BY MINISTRY;
