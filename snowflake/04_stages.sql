/*=============================================================================
  Government Information Analytics Platform - Snowflake Migration
  File: 04_stages.sql
  Purpose: Define the internal stage for weighted ministry report files.
  Author: Jonathan Mukundu
  Date: 2026-07-21

  Revision History:
  - 2026-07-20 | Jonathan Mukundu | Initial scaffold.
  - 2026-07-21 | Jonathan Mukundu | Implemented ministry report internal stage.
=============================================================================*/

USE ROLE ACCOUNTADMIN;
USE WAREHOUSE GOV_MIS_WH;
USE DATABASE GOVERNMENT_MIS;

CREATE STAGE IF NOT EXISTS GOVERNMENT_MIS.RAW.MINISTRY_REPORTS_STAGE
    FILE_FORMAT = GOVERNMENT_MIS.RAW.MINISTRY_REPORTS_CSV_FORMAT
    COMMENT = 'Internal stage for MCTI and MGEE weighted ministry CSV files';

-- Upload both source files to the root of this stage manually through Snowsight
-- or SnowSQL. Local workspace files cannot be uploaded by this SQL script.
LIST @GOVERNMENT_MIS.RAW.MINISTRY_REPORTS_STAGE;

SHOW STAGES LIKE 'MINISTRY_REPORTS_STAGE'
    IN SCHEMA GOVERNMENT_MIS.RAW;
