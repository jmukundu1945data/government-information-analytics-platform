import random
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

MCTI_OUT = ROOT / "MCTI" / "raw_submissions" / "MCTI_WEIGHTED_2025_2026.csv"
MGEE_OUT = ROOT / "MGEE" / "raw_submissions" / "MGEE_WEIGHTED_2025_2026.csv"

random.seed(42)

# =========================================================
# GEOGRAPHY
# =========================================================

districts = {
    "Lusaka": ["Lusaka", "Chongwe", "Kafue", "Rufunsa"],
    "Copperbelt": ["Ndola", "Kitwe", "Chingola", "Mufulira", "Luanshya"],
    "Southern": ["Livingstone", "Choma", "Mazabuka", "Monze"],
    "Eastern": ["Chipata", "Katete", "Petauke", "Lundazi"],
    "Central": ["Kabwe", "Kapiri Mposhi", "Mkushi"],
    "North-Western": ["Solwezi", "Kalumbila", "Mwinilunga"],
    "Western": ["Mongu", "Senanga"],
    "Luapula": ["Mansa", "Samfya"],
    "Northern": ["Kasama", "Mbala"],
    "Muchinga": ["Chinsali"],
}

province_weights = {
    "Lusaka": 1.80,
    "Copperbelt": 1.45,
    "Southern": 1.30,
    "Eastern": 1.25,
    "Central": 1.00,
    "North-Western": 0.90,
    "Western": 0.70,
    "Luapula": 0.65,
    "Northern": 0.65,
    "Muchinga": 0.55,
}

periods = [
    "2025M01", "2025M02", "2025M03",
    "2025M04", "2025M05", "2025M06",
    "2025M07", "2025M08", "2025M09",
    "2025M10", "2025M11", "2025M12",
]

# =========================================================
# MCTI PROGRAMS & INDICATORS
# =========================================================

mcti_programs = [
    ("MCTI001", "MSME Development"),
    ("MCTI002", "Trade Facilitation"),
    ("MCTI003", "Industrial Development"),
    ("MCTI004", "Export Promotion"),
]

mcti_indicators = [
    ("MCTI_IND_001", "SMEs Supported", 300, 1200),
    ("MCTI_IND_002", "Businesses Trained", 200, 900),
    ("MCTI_IND_003", "Youth Entrepreneurs Supported", 100, 700),
    ("MCTI_IND_004", "Market Linkages Facilitated", 50, 300),
    ("MCTI_IND_005", "Export Certifications Processed", 20, 120),
    ("MCTI_IND_006", "Trade Inspections Conducted", 40, 250),
]

# =========================================================
# MGEE PROGRAMS & INDICATORS
# =========================================================

mgee_programs = [
    ("MGEE001", "Climate Adaptation"),
    ("MGEE002", "Environmental Compliance"),
    ("MGEE003", "Forestry Restoration"),
    ("MGEE004", "Green Economy"),
]

mgee_indicators = [
    ("MGEE_IND_001", "Environmental Inspections", 20, 120),
    ("MGEE_IND_002", "Climate Adaptation Activities", 10, 80),
    ("MGEE_IND_003", "Community Trainings Conducted", 20, 150),
    ("MGEE_IND_004", "Forestry Restoration Projects", 5, 40),
    ("MGEE_IND_005", "Environmental Compliance Reviews", 10, 60),
]

# =========================================================
# GENERATOR FUNCTION
# =========================================================

def generate_rows(ministry, programs, indicators, ministry_weight):

    rows = []

    # Province-level data quality risk
    dq_risk = {
        "Lusaka": 0.01,
        "Copperbelt": 0.015,
        "Southern": 0.02,
        "Eastern": 0.025,
        "Central": 0.03,
        "North-Western": 0.04,
        "Western": 0.05,
        "Luapula": 0.055,
        "Northern": 0.055,
        "Muchinga": 0.07,
    }

    for period in periods:

        for province, district_list in districts.items():

            province_weight = province_weights[province]
            risk = dq_risk[province]

            for district in district_list:

                for program_id, program_name in programs:

                    for indicator_code, indicator_name, low, high in indicators:

                        base_target = random.randint(low, high)

                        target = int(
                            base_target
                            * province_weight
                            * ministry_weight
                        )

                        performance_factor = random.uniform(0.85, 1.10)
                        reported = int(target * performance_factor)

                        # -----------------------------
                        # Controlled data quality defects
                        # -----------------------------
                        issue_roll = random.random()

                        if issue_roll < risk:
                            reported = None

                        elif issue_roll < risk * 1.5:
                            target = None

                        elif issue_roll < risk * 1.8:
                            reported = -abs(reported)

                        elif issue_roll < risk * 2.0:
                            target = -abs(target)

                        rows.append({
                            "reporting_period": period,
                            "province": province,
                            "district": district,
                            "program_id": program_id,
                            "program_name": program_name,
                            "indicator_code": indicator_code,
                            "indicator_name": indicator_name,
                            "reported_value": reported,
                            "target_value": target,
                            "reporting_officer": f"{district} Reporting Officer",
                            "submission_date": "2026-01-15",
                            "submission_status": "Submitted"
                        })

    return pd.DataFrame(rows)
# =========================================================
# GENERATE DATASETS
# =========================================================

# MCTI intentionally stronger operational footprint
mcti_df = generate_rows(
    "MCTI",
    mcti_programs,
    mcti_indicators,
    ministry_weight=1.5
)

# MGEE moderate institutional footprint
mgee_df = generate_rows(
    "MGEE",
    mgee_programs,
    mgee_indicators,
    ministry_weight=9.4
)

# Add ministry column
mcti_df["ministry"] = "MCTI"
mgee_df["ministry"] = "MGEE"

# =========================================================
# SAVE FILES
# =========================================================

mcti_df.to_csv(MCTI_OUT, index=False)
mgee_df.to_csv(MGEE_OUT, index=False)

print("=" * 60)
print("SIMULATION DATA GENERATED")
print("=" * 60)

print(f"MCTI rows: {len(mcti_df):,}")
print(f"MGEE rows: {len(mgee_df):,}")

print()
print("TOTAL REPORTED VALUES")

print(f"MCTI: {mcti_df['reported_value'].sum():,}")
print(f"MGEE: {mgee_df['reported_value'].sum():,}")

print("=" * 60)