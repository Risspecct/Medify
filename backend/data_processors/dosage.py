from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

dosage_file_path = os.getenv("DOSAGE_FILE_PATH", "datasets/dosage.csv")


def load_dosage_data(filepath: str = dosage_file_path) -> pd.DataFrame | str:
    """Load dosage dataset, skipping bad rows."""
    try:
        return pd.read_csv(filepath, on_bad_lines="skip")
    except FileNotFoundError:
        return f"Error: The file '{filepath}' was not found."


def find_medicine(df: pd.DataFrame, medicine_name: str) -> pd.DataFrame:
    """Find medicine by generic or brand name (case-insensitive)."""
    med = df[df["drug_generic"].str.lower() == medicine_name.lower()]
    if med.empty:
        med = df[df["common_brands_india"].str.lower().str.contains(medicine_name.lower(), na=False)]
    return med


def get_med_info(medicine_name: str, age_in_months: int) -> dict | str:
    """Retrieve full dosage info for a medicine at a given age."""
    df = load_dosage_data()
    if isinstance(df, str):  # Error while loading
        return df

    med = find_medicine(df, medicine_name)
    if med.empty:
        return f"Medicine '{medicine_name}' not found."

    row = med.iloc[0]  # take first match
    min_age, max_age = row["min_age_months"], row["max_age_months"]

    if pd.notna(min_age) and pd.notna(max_age):
        if not (min_age <= age_in_months <= max_age):
            return (f"The age {age_in_months} months is not within the supported range "
                    f"for {row['drug_generic']} ({min_age}-{max_age} months).")

    return row.to_dict()


def get_dosage(medicine_name: str, age_in_months: int) -> dict | str:
    """Return only dosage-related info (subset of medicine data)."""
    required_fields = [
        "drug_generic",
        "max_daily_dose",
        "max_daily_dose_units",
        "notes_key_safety",
        "dosing_interval_hours",
    ]

    med_info = get_med_info(medicine_name, age_in_months)
    if isinstance(med_info, str):  # error
        return med_info

    return {field: med_info.get(field) for field in required_fields}


# print(get_dosage("Tramadol", 1000))
# print("_" * 40)
# print(get_dosage("ventolin", 144))
