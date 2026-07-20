# Snowflake Migration

## Purpose

This folder contains the scaffold for migrating the Government Information Analytics Platform to Snowflake. It organizes the future implementation into ordered scripts for environment setup, raw data structures, file formats, stages, data loading, validation, and reporting views, together with Power BI connection and migration documentation.

The current contents are intentionally placeholders only. No Snowflake objects, data-loading commands, or executable migration SQL have been defined yet.

## File sequence

1. `01_environment.sql` — environment, roles, database, schemas, and warehouses
2. `02_raw_tables.sql` — raw-layer table definitions
3. `03_file_formats.sql` — source file format definitions
4. `04_stages.sql` — internal or external stage definitions
5. `05_load_raw_data.sql` — raw-data loading operations
6. `06_validation.sql` — migration validation and reconciliation
7. `07_views.sql` — analytics and reporting views
8. `08_powerbi_connection.md` — Power BI connectivity guidance
9. `09_migration_notes.md` — decisions, risks, assumptions, and cutover notes
10. `MIGRATION_LOG.md` — sprint-level migration progress

## Implementation status

Sprint 1 establishes the migration project structure. Future sprints will replace TODO placeholders with reviewed and approved implementation details.

## Usage

TODO: Add execution prerequisites, deployment order, review controls, and environment-specific guidance when implementation begins.

