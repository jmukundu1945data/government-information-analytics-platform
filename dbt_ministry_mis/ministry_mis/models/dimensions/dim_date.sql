{{ config(materialized='table') }}

with dates as (

    select *
    from generate_series(
        date '2025-01-01',
        date '2025-12-31',
        interval 1 day
    ) as t(date_day)

)

select
    cast(strftime(date_day, '%Y%m%d') as integer) as date_key,
    cast(date_day as date) as date,
    year(date_day) as year,
    month(date_day) as month_number,
    strftime(date_day, '%B') as month_name,
    'Q' || quarter(date_day)::varchar as quarter,
    strftime(date_day, '%Y-%m') as year_month
from dates
