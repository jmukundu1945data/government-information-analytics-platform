{{ config(materialized='table') }}

select distinct
    province
from {{ ref('stg_ministry_reports') }}
