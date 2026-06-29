import duckdb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB_FILE = ROOT / "database" / "ministry_mis.duckdb"

con = duckdb.connect(str(DB_FILE))

# =====================================================
# SEMANTIC MART: Ministry Performance Summary
# =====================================================

con.execute("""
CREATE OR REPLACE VIEW mart_ministry_performance AS

SELECT
    ministry,
    reporting_period,
    province,
    district,
    program_id,
    indicator_code,
    indicator_name,
    SUM(reported_value) AS reported_value,
    SUM(target_value) AS target_value,
    SUM(reported_value) - SUM(target_value) AS variance,
    CASE
        WHEN SUM(target_value) = 0 THEN NULL
        ELSE ROUND((SUM(reported_value) / SUM(target_value)) * 100, 1)
    END AS achievement_percent
FROM raw_ministry_reports
GROUP BY
    ministry,
    reporting_period,
    province,
    district,
    program_id,
    indicator_code,
    indicator_name
;
""")

# =====================================================
# SEMANTIC MART: Executive Summary
# =====================================================

con.execute("""
CREATE OR REPLACE VIEW mart_executive_summary AS

SELECT
    ministry,
    reporting_period,
    province,
    COUNT(DISTINCT district) AS districts_reporting,
    COUNT(DISTINCT program_id) AS programs_reporting,
    COUNT(DISTINCT indicator_code) AS indicators_reported,
    SUM(reported_value) AS total_reported_value,
    SUM(target_value) AS total_target_value,
    SUM(reported_value) - SUM(target_value) AS total_variance
FROM raw_ministry_reports
GROUP BY
    ministry,
    reporting_period,
    province
;
""")

# =====================================================
# TEST OUTPUT
# =====================================================

print("=== MART: MINISTRY PERFORMANCE ===")
print(con.execute("""
SELECT *
FROM mart_ministry_performance
ORDER BY ministry, province, district
""").fetchdf())

print("\n=== MART: EXECUTIVE SUMMARY ===")
print(con.execute("""
SELECT *
FROM mart_executive_summary
ORDER BY ministry, province
""").fetchdf())

con.close()

print("\nSemantic marts created successfully.")
