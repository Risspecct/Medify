import pandas as pd
import re
from typing import Dict, Any


def _check_symptom(df: pd.DataFrame, symptom: str, medicine_name: str, report: Dict[str, Any]) -> None:
    """Check if the medicine is listed for the given symptom."""
    symptom_meds = df[df['symptoms_indications'].str.contains(symptom, case=False, na=False)]

    if symptom_meds.empty:
        report["symptom_check"] = f"No medicines found for symptom '{symptom}' in the dataset."
        return

    if medicine_name.lower() not in symptom_meds['drug_generic'].str.lower().values:
        recommended = ", ".join(symptom_meds['drug_generic'].unique())
        report["symptom_check"] = (
            f"Warning: {medicine_name} is not listed for '{symptom}'. Suggested alternatives: {recommended}."
        )
    else:
        report["symptom_check"] = f"Pass: {medicine_name} is listed as a treatment for '{symptom}'."


def _check_age(medicine_info: pd.Series, age_in_months: int, report: Dict[str, Any]) -> None:
    """Check if the patient's age is within the recommended range."""
    min_age, max_age = medicine_info['min_age_months'], medicine_info['max_age_months']

    if pd.notna(min_age) and pd.notna(max_age):
        if not min_age <= age_in_months <= max_age:
            report["age_check"] = (
                f"Fail: Age {age_in_months} months is outside the recommended range "
                f"({min_age}-{max_age} months)."
            )
        else:
            report["age_check"] = "Pass: Age is within the recommended range."
    else:
        report["age_check"] = "Not applicable: No age restrictions found."


def _check_dosage(medicine_info: pd.Series, given_dose: float, medicine_name: str, report: Dict[str, Any]) -> None:
    """Check if the given dosage is within the recommended range."""
    dose_range_str = medicine_info['dose_mg_per_kg']

    if pd.isna(dose_range_str) or not isinstance(dose_range_str, str):
        report["dosage_check"] = "Not applicable: No mg/kg dosage specified in dataset."
        return

    # Extract numbers from strings like '10-15' or '5'
    values = [float(x) for x in re.findall(r'[\d\.]+', dose_range_str)]
    min_dose, max_dose = values[0], values[-1]

    if not min_dose <= given_dose <= max_dose:
        report["dosage_check"] = (
            f"Fail: {given_dose} mg/kg is outside recommended range {dose_range_str} mg/kg."
        )
    else:
        report["dosage_check"] = "Pass: Dosage is within the recommended range."

    report["notes"].append(f"Recommended dose range for {medicine_name}: {dose_range_str} mg/kg.")


def get_report(symptom: str, medicine_name: str, age_in_months: int, given_dosage_mg_per_kg: float) -> Dict[str, Any]:
    """
    Verifies a treatment plan against the dosage.csv dataset.

    Args:
        symptom: Symptom being treated (e.g., "Fever").
        medicine_name: Generic name of the medicine (e.g., "Paracetamol").
        age_in_months: Patient's age in months.
        given_dosage_mg_per_kg: Administered dosage in mg/kg.

    Returns:
        A structured verification report.
    """
    report = {
        "symptom_check": "Pending",
        "age_check": "Pending",
        "dosage_check": "Pending",
        "notes": [],
        "disclaimer": (
            "This verification is based on a reference dataset. "
            "It is NOT a substitute for professional medical advice. Consult a doctor."
        )
    }

    try:
        df = pd.read_csv("C:\\Users\\Rishi\\Desktop\\Program related\\Medify\\datasets\\dosage.csv", on_bad_lines="skip")
    except FileNotFoundError:
        report["notes"].append("Error: The 'dosage.csv' file was not found.")
        return report

    # Symptom check
    _check_symptom(df, symptom, medicine_name, report)

    # Find medicine info
    medicine_data = df[df['drug_generic'].str.lower() == medicine_name.lower()]
    if medicine_data.empty:
        report["notes"].append(f"Medicine '{medicine_name}' not found in dataset.")
        return report

    # Use first record for verification
    medicine_info = medicine_data.iloc[0]

    # Age and dosage checks
    _check_age(medicine_info, age_in_months, report)
    _check_dosage(medicine_info, given_dosage_mg_per_kg, medicine_name, report)

    return report


# Example usage:
print(get_report("Fever", "Paracetamol", 240, 15))
