/*=============================================================================
  Government Information Analytics Platform - Snowflake Migration
  File: 03_file_formats.sql
  Purpose: Define the CSV file format for weighted ministry report files.
  Author: Jonathan Mukundu
  Date: 2026-07-21

  Revision History:
  - 2026-07-20 | Jonathan Mukundu | Initial scaffold.
  - 2026-07-21 | Jonathan Mukundu | Implemented weighted ministry CSV format.
=============================================================================*/

USE ROLE ACCOUNTADMIN;
USE WAREHOUSE GOV_MIS_WH;
USE DATABASE GOVERNMENT_MIS;

CREATE OR REPLACE FILE FORMAT GOVERNMENT_MIS.RAW.MINISTRY_REPORTS_CSV_FORMAT
    TYPE = CSV
    FIELD_DELIMITER = ','
    SKIP_HEADER = 1
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    ESCAPE_UNENCLOSED_FIELD = NONE
    EMPTY_FIELD_AS_NULL = TRUE
    NULL_IF = ('', 'NULL', 'null')
    ENCODING = 'UTF8';

SHOW FILE FORMATS LIKE 'MINISTRY_REPORTS_CSV_FORMAT'
    IN SCHEMA GOVERNMENT_MIS.RAW;
