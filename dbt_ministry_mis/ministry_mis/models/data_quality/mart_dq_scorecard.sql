{{ config(materialized='view') }}

select
    ministry,
    reporting_period,
    date_key,
    province,
    count(*) as total_records,

    sum(case when reported_value is null then 1 else 0 end) as missing_reported_values,
    sum(case when target_value is null then 1 else 0 end) as missing_target_values,
    sum(case when reported_value < 0 then 1 else 0 end) as negative_reported_values,
    sum(case when target_value < 0 then 1 else 0 end) as negative_target_values,

    count(distinct district) as districts_reporting,

    round(
        100.0 *
        (
            count(*)
            - sum(case when reported_value is null then 1 else 0 end)
            - sum(case when target_value is null then 1 else 0 end)
            - sum(case when reported_value < 0 then 1 else 0 end)
            - sum(case when target_value < 0 then 1 else 0 end)
        ) / count(*),
        1
    ) as dq_score_percent

from {{ ref('stg_ministry_reports') }}
group by
    ministry,
    reporting_period,
    date_key,
    province
