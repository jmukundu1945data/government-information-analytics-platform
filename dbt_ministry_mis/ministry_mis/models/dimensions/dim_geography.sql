{{ config(materialized='table') }}

select distinct
    province,
    district
from {{ ref('stg_ministry_reports') }}
