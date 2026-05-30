{{ config(materialized='view') }}

select
    ministry,
    reporting_period,
    date_key,
    province,
    total_records,
    missing_reported_values,
    missing_target_values,
    negative_reported_values,
    negative_target_values,
    districts_reporting,
    dq_score_percent
from {{ ref('mart_dq_scorecard') }}
