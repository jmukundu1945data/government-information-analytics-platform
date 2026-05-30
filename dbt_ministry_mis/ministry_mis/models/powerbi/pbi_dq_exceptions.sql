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
    reported_value,
    target_value,

    case
        when reported_value is null then 'Missing reported value'
        when reported_value < 0 then 'Negative reported value'
        when target_value is null then 'Missing target value'
        when target_value < 0 then 'Negative target value'
        else 'No issue'
    end as dq_issue_type,

    1 as dq_exception_flag

from {{ ref('stg_ministry_reports') }}

where
    reported_value is null
    or reported_value < 0
    or target_value is null
    or target_value < 0
