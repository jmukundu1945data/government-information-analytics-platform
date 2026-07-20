/*=============================================================================
  Government Information Analytics Platform - Snowflake Migration
  File: 02_raw_tables.sql
  Purpose: Create the raw ministry reports table in Snowflake.
  Author: Jonathan Mukundu
  Date: 2026-07-20

  Revision History:
  - 2026-07-20 | Jonathan Mukundu | Created RAW_MINISTRY_REPORTS table.
=============================================================================*/

USE DATABASE GOVERNMENT_MIS;
USE SCHEMA RAW;

CREATE TABLE IF NOT EXISTS RAW.RAW_MINISTRY_REPORTS (
    MINISTRY VARCHAR,
    SOURCE_FILE VARCHAR,
    REPORTING_PERIOD VARCHAR,
    PROVINCE VARCHAR,
    DISTRICT VARCHAR,
    PROGRAM_ID VARCHAR,
    INDICATOR_CODE VARCHAR,
    INDICATOR_NAME VARCHAR,
    REPORTED_VALUE FLOAT,
    TARGET_VALUE FLOAT,
    REPORTING_OFFICER VARCHAR,
    SUBMISSION_DATE DATE,
    INGESTION_TIMESTAMP TIMESTAMP_NTZ
);

DESCRIBE TABLE RAW.RAW_MINISTRY_REPORTS;
