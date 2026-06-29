import duckdb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB_FILE = ROOT / "database" / "ministry_mis.duckdb"

con = duckdb.connect(str(DB_FILE))

print("=== RAW TABLE PREVIEW ===")
print(con.execute("""
SELECT *
FROM raw_ministry_reports
LIMIT 10
""").fetchdf())

print("\n=== RECORDS BY MINISTRY ===")
print(con.execute("""
SELECT
    ministry,
    COUNT(*) AS total_records
FROM raw_ministry_reports
GROUP BY ministry
""").fetchdf())

print("\n=== PERFORMANCE SUMMARY ===")
print(con.execute("""
SELECT
    ministry,
    province,
    program_id,
    indicator_code,
    SUM(reported_value) AS reported_value,
    SUM(target_value) AS target_value,
    SUM(reported_value) - SUM(target_value) AS variance
FROM raw_ministry_reports
GROUP BY
    ministry,
    province,
    program_id,
    indicator_code
ORDER BY
    ministry,
    province,
    program_id,
    indicator_code
""").fetchdf())

con.close()
