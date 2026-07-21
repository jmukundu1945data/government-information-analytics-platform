# Snowflake Migration Log

## Sprint 1 — Completed

Date: 2026-07-20

- Created the Snowflake migration scaffold.
- Added ordered SQL placeholder files for the planned migration workflow.
- Added Power BI connection and migration notes placeholders.
- Added migration overview and progress documentation.
- Confirmed that no migration SQL has been implemented in this sprint.

### Sprint 1 Notes

Snowflake SQL files must be executed using **Run All**
(Ctrl + Shift + Enter).

Running only the current statement may result in missing
database/schema context because previous statements (CREATE, USE)
have not been executed.

## Sprint 2 — Generated, pending execution verification

Date generated: 2026-07-21

Owner: Jonathan Mukundu

- Implemented the shared CSV file format for the MCTI and MGEE weighted files.
- Implemented the internal ministry report stage and stage verification queries.
- Implemented the explicit-column `COPY INTO` load for both weighted source files.
- Added row-count, ministry reconciliation, value-quality, and duplicate checks.
- Documented `07_views.sql` as an intentional no-op because dbt owns modeled views.
- Confirmed local source expectations: MCTI = 8,640, MGEE = 7,200, total = 15,840.

### Sprint 2 execution status

Not complete. The SQL has been generated but has not been executed in Snowflake.
Upload `MCTI_WEIGHTED_2025_2026.csv` and `MGEE_WEIGHTED_2025_2026.csv` manually to
the root of `@GOVERNMENT_MIS.RAW.MINISTRY_REPORTS_STAGE` through Snowsight or
SnowSQL before running `05_load_raw_data.sql`. Mark this sprint complete only
after the load and `06_validation.sql` results have been verified.

## Sprint 3 — Planned

TODO: Define scope, deliverables, owners, dates, validation, and completion status.

## Future sprints

TODO: Add future sprint sections as the migration plan is approved.
