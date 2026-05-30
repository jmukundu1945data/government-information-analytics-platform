{{ config(materialized='table') }}

select distinct
    ministry
from {{ ref('stg_ministry_reports') }}
