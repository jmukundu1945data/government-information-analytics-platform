{{ config(materialized='table') }}

select
    ministry,
    reporting_period,
    date_key,
    province,
    district,
    program_id,
    indicator_code,
    indicator_name,
    reported_value,
    target_value,
    variance,
    achievement_percent
from {{ ref('mart_ministry_performance') }}
