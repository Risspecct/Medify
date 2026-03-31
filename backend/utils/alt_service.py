from datasets.alt_dataset import get_dataset_alt

KB = get_dataset_alt()


def find_med_and_calculate_savings(name: str):
    name = name.lower()
    for key, data in KB.items():
        if key in name:
            base_price = data.get("price_in_inr", 0)
            if base_price > 0:
                for alt in data.get("alternatives", []):
                    alt_price = alt.get("price_in_inr", 0)
                    alt["savings_percentage"] = round(((base_price - alt_price) / base_price) * 100, 2)
            return data
    return None
