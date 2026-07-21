/*=============================================================================
  Government Information Analytics Platform - Snowflake Migration
  File: 07_views.sql
  Purpose: Document raw-layer view ownership for the Snowflake migration.
  Author: Jonathan Mukundu
  Date: 2026-07-21

  Revision History:
  - 2026-07-20 | Jonathan Mukundu | Initial scaffold.
  - 2026-07-21 | Jonathan Mukundu | Documented intentional raw-view no-op.
=============================================================================*/

USE ROLE ACCOUNTADMIN;
USE WAREHOUSE GOV_MIS_WH;
USE DATABASE GOVERNMENT_MIS;

-- INTENTIONAL NO-OP
-- No raw-layer convenience view is required before the dbt migration.
-- dbt remains the owner of staging, dimensions, marts, data-quality models,
-- and Power BI-facing views. Defining those objects here would duplicate the
-- existing dbt business logic.
