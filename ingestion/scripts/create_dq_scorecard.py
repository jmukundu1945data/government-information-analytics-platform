import duckdb

DB_FILE = r"C:\DAI_MIS_SIMULATION\database\ministry_mis.duckdb"

con = duckdb.connect(DB_FILE)

con.execute("""
CREATE OR REPLACE VIEW mart_dq_scorecard AS

SELECT
    ministry,
    reporting_period,
    province,

    COUNT(*) AS total_records,

    SUM(CASE WHEN reported_value IS NULL THEN 1 ELSE 0 END) AS missing_reported_values,

    SUM(CASE WHEN target_value IS NULL THEN 1 ELSE 0 END) AS missing_target_values,

    SUM(CASE WHEN reported_value < 0 THEN 1 ELSE 0 END) AS negative_reported_values,

    SUM(CASE WHEN target_value < 0 THEN 1 ELSE 0 END) AS negative_target_values,

    COUNT(DISTINCT district) AS districts_reporting,

    ROUND(
        100.0 *
        (
            COUNT(*)
            - SUM(CASE WHEN reported_value IS NULL THEN 1 ELSE 0 END)
            - SUM(CASE WHEN target_value IS NULL THEN 1 ELSE 0 END)
            - SUM(CASE WHEN reported_value < 0 THEN 1 ELSE 0 END)
            - SUM(CASE WHEN target_value < 0 THEN 1 ELSE 0 END)
        ) / COUNT(*),
        1
    ) AS dq_score_percent

FROM raw_ministry_reports

GROUP BY
    ministry,
    reporting_period,
    province
;
""")

print("=== DQ SCORECARD ===")
print(con.execute("""
SELECT *
FROM mart_dq_scorecard
ORDER BY ministry, province
""").fetchdf())

con.close()

print("\nDQ scorecard created successfully.")
