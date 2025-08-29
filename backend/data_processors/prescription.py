import pandas as pd
import re


def get_report(symptom: str, medicine_name: str, age_in_months: int, given_dosage_mg_per_kg: float):
    """
    Verifies a given treatment plan against the dosage.csv dataset.

    Args:
        symptom: The symptom being treated (e.g., "Fever").
        medicine_name: The generic name of the medicine given (e.g., "Paracetamol").
        age_in_months: The patient's age in months.
        given_dosage_mg_per_kg: The dosage administered in mg per kg.

    Returns:
        A dictionary containing the verification report.
    """
    report = {
        "symptom_check": "Pending",
        "age_check": "Pending",
        "dosage_check": "Pending",
        "notes": [],
        "disclaimer": "This is a verification against a reference dataset, NOT a substitute for professional medical advice. Consult a doctor for any health concerns."
    }

    try:
        df = pd.read_csv('dosage.csv', on_bad_lines='skip')
    except FileNotFoundError:
        report["notes"].append("Error: The 'dosage.csv' file was not found.")
        return report

    # 1. Symptom Check
    symptom_medicines = df[df['symptoms_indications'].str.contains(symptom, case=False, na=False)]
    if symptom_medicines.empty:
        report["symptom_check"] = f"No medicines found for symptom '{symptom}' in the dataset."
    elif medicine_name.lower() not in symptom_medicines['drug_generic'].str.lower().values:
        recommended_drugs = ", ".join(symptom_medicines['drug_generic'].unique())
        report["symptom_check"] = f"Warning: {medicine_name} is not listed for '{symptom}'. The dataset suggests: {recommended_drugs}."
    else:
        report["symptom_check"] = f"Pass: {medicine_name} is listed as a potential treatment for '{symptom}'."

    # 2. Medicine-Specific Age and Dosage Check
    medicine_info = df[df['drug_generic'].str.lower() == medicine_name.lower()]

    if medicine_info.empty:
        report["notes"].append(f"Medicine '{medicine_name}' not found in the dataset.")
        return report

    # Extract single record for the medicine
    medicine_info = medicine_info.iloc[0]

    # Age Check
    min_age, max_age = medicine_info['min_age_months'], medicine_info['max_age_months']
    if pd.notna(min_age) and pd.notna(max_age):
        if not min_age <= age_in_months <= max_age:
            report["age_check"] = f"Fail: Age {age_in_months} months is outside the recommended range ({min_age}-{max_age} months)."
        else:
            report["age_check"] = "Pass: Age is within the recommended range."

    # Dosage Check
    dose_range_str = medicine_info['dose_mg_per_kg']
    if pd.isna(dose_range_str) or not isinstance(dose_range_str, str):
        report["dosage_check"] = "Not applicable: The dataset does not specify a mg/kg dosage for this medicine."
    else:
        # Extract numbers from strings like '10-15' or '5'
        dose_values = [float(x) for x in re.findall(r'[\d\.]+', dose_range_str)]
        min_dose = dose_values[0]
        max_dose = dose_values[-1]  # Handles single numbers and ranges

        if not min_dose <= given_dosage_mg_per_kg <= max_dose:
            report["dosage_check"] = (f"Fail: Given dosage of {given_dosage_mg_per_kg} mg/kg is outside "
                                      f"the recommended range of {dose_range_str} mg/kg.")
        else:
            report["dosage_check"] = "Pass: Dosage is within the recommended range."
        report["notes"].append(f"Recommended dose range for {medicine_name}: {dose_range_str} mg/kg.")

    return report


"""
--- Example Usage ---


# Example 1: Everything looks correct
print("--- Scenario 1: Correct Treatment ---")
report1 = verify_treatment(symptom="Fever", medicine_name="Ibuprofen", age_in_months=24, given_dosage_mg_per_kg=8)
for key, value in report1.items():
    print(f"{key.replace('_', ' ').title()}: {value}")

print("\n" + "=" * 40 + "\n")

# Example 2: Dosage is too high
print("--- Scenario 2: High Dosage ---")
report2 = verify_treatment(symptom="Pain", medicine_name="Paracetamol", age_in_months=12, given_dosage_mg_per_kg=20)
for key, value in report2.items():
    print(f"{key.replace('_', ' ').title()}: {value}")

print("\n" + "=" * 40 + "\n")

# Example 3: Medicine does not match symptom in the dataset
print("--- Scenario 3: Mismatched Medicine ---")
report3 = verify_treatment(symptom="Bacterial skin infections", medicine_name="Paracetamol", age_in_months=36, given_dosage_mg_per_kg=15)
for key, value in report3.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
"""
