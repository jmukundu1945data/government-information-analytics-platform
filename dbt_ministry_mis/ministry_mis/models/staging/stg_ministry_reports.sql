{{ config(materialized='view') }}

select
    ministry,
    source_file,
    reporting_period,
    cast(left(reporting_period, 4) || right(reporting_period, 2) || '01' as integer) as date_key,
    province,
    district,
    program_id,
    indicator_code,
    indicator_name,
    cast(reported_value as double) as reported_value,
    cast(target_value as double) as target_value,
    reporting_officer,
    cast(submission_date as date) as submission_date,
    ingestion_timestamp
from raw_ministry_reports
