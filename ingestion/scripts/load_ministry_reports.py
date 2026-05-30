import pandas as pd
import duckdb
from pathlib import Path
from datetime import datetime

# =====================================================
# CONFIGURATION
# =====================================================

ROOT = Path(r"C:\DAI_MIS_SIMULATION")

MCTI_FOLDER = ROOT / "MCTI" / "raw_submissions"
MGEE_FOLDER = ROOT / "MGEE" / "raw_submissions"

GEOGRAPHY_FILE = ROOT / "shared_reference" / "geography" / "ref_geography.csv"

DB_FILE = ROOT / "database" / "ministry_mis.duckdb"

VALIDATED_FOLDER = ROOT / "ingestion" / "validated"
REJECTED_FOLDER = ROOT / "ingestion" / "rejected"

# =====================================================
# LOAD REFERENCE DATA
# =====================================================

geo_df = pd.read_csv(GEOGRAPHY_FILE)

valid_geo = set(
    zip(
        geo_df["province_name"].str.upper(),
        geo_df["district_name"].str.upper()
    )
)

# =====================================================
# CONNECT TO DUCKDB
# =====================================================

con = duckdb.connect(str(DB_FILE))

# =====================================================
# CREATE TABLES
# =====================================================

con.execute("""

CREATE TABLE IF NOT EXISTS raw_ministry_reports (

    ministry VARCHAR,
    source_file VARCHAR,
    reporting_period VARCHAR,
    province VARCHAR,
    district VARCHAR,
    program_id VARCHAR,
    indicator_code VARCHAR,
    indicator_name VARCHAR,
    reported_value DOUBLE,
    target_value DOUBLE,
    reporting_officer VARCHAR,
    submission_date DATE,
    ingestion_timestamp TIMESTAMP

)

""")

# =====================================================
# VALIDATION FUNCTION
# =====================================================

def validate_geography(row):

    key = (
        str(row["province"]).upper(),
        str(row["district"]).upper()
    )

    return key in valid_geo

# =====================================================
# PROCESS FILES
# =====================================================

def process_folder(folder_path, ministry_name):

    csv_files = list(folder_path.glob("*.csv"))

    for file in csv_files:

        print(f"\nProcessing: {file.name}")

        df = pd.read_csv(file)

        df["is_valid_geo"] = df.apply(validate_geography, axis=1)

        invalid_rows = df[df["is_valid_geo"] == False]
        valid_rows = df[df["is_valid_geo"] == True]

        # ---------------------------------------------
        # SAVE INVALID RECORDS
        # ---------------------------------------------

        if len(invalid_rows) > 0:

            rejected_file = REJECTED_FOLDER / f"REJECTED_{file.name}"

            invalid_rows.to_csv(rejected_file, index=False)

            print(f"Rejected rows: {len(invalid_rows)}")

        # ---------------------------------------------
        # LOAD VALID RECORDS
        # ---------------------------------------------

        if len(valid_rows) > 0:

            valid_rows["ministry"] = ministry_name
            valid_rows["source_file"] = file.name
            valid_rows["ingestion_timestamp"] = datetime.now()

            load_cols = [
                "ministry",
                "source_file",
                "reporting_period",
                "province",
                "district",
                "program_id",
                "indicator_code",
                "indicator_name",
                "reported_value",
                "target_value",
                "reporting_officer",
                "submission_date",
                "ingestion_timestamp"
            ]

            final_df = valid_rows[load_cols]

            con.register("temp_df", final_df)

            con.execute("""

                INSERT INTO raw_ministry_reports
                SELECT * FROM temp_df

            """)

            validated_file = VALIDATED_FOLDER / f"VALIDATED_{file.name}"

            valid_rows.to_csv(validated_file, index=False)

            print(f"Loaded rows: {len(valid_rows)}")

# =====================================================
# RUN PIPELINE
# =====================================================

process_folder(MCTI_FOLDER, "MCTI")
process_folder(MGEE_FOLDER, "MGEE")

# =====================================================
# SUMMARY
# =====================================================

summary = con.execute("""

SELECT
    ministry,
    COUNT(*) AS total_records
FROM raw_ministry_reports
GROUP BY ministry

""").fetchdf()

print("\n===== LOAD SUMMARY =====")
print(summary)

con.close()

print("\nPipeline completed successfully.")