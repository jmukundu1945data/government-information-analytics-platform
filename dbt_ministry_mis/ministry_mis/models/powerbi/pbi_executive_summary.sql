{{ config(materialized='view') }}

select
    ministry,
    reporting_period,
    province,
    districts_reporting,
    programs_reporting,
    indicators_reported,
    total_reported_value,
    total_target_value,
    total_variance
from {{ ref('mart_executive_summary') }}
