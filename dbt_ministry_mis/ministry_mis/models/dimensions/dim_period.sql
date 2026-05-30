{{ config(materialized='table') }}

select distinct
    reporting_period,
    left(reporting_period, 4) as reporting_year,
    right(reporting_period, 2) as reporting_month,
    cast(left(reporting_period, 4) || right(reporting_period, 2) || '01' as integer) as date_key
from {{ ref('stg_ministry_reports') }}
