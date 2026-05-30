{{ config(materialized='view') }}

select
    ministry,
    reporting_period,
    province,
    count(distinct district) as districts_reporting,
    count(distinct program_id) as programs_reporting,
    count(distinct indicator_code) as indicators_reported,
    sum(reported_value) as total_reported_value,
    sum(target_value) as total_target_value,
    sum(reported_value) - sum(target_value) as total_variance
from {{ ref('stg_ministry_reports') }}
group by
    ministry,
    reporting_period,
    province
