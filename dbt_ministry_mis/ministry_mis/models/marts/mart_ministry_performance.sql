{{ config(materialized='view') }}

select
    ministry,
    reporting_period,
    date_key,
    province,
    district,
    program_id,
    indicator_code,
    indicator_name,
    sum(reported_value) as reported_value,
    sum(target_value) as target_value,
    sum(reported_value) - sum(target_value) as variance,
    case
        when sum(target_value) = 0 then null
        else round((sum(reported_value) / sum(target_value)) * 100, 1)
    end as achievement_percent
from {{ ref('stg_ministry_reports') }}
group by
    ministry,
    reporting_period,
    date_key,
    province,
    district,
    program_id,
    indicator_code,
    indicator_name
