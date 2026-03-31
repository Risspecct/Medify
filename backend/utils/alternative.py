from backend.datasets.alt_dataset import get_dataset_alt
ALTERNATIVE_KNOWLEDGE_BASE = get_dataset_alt()


def find_alternatives(medication_name: str) -> dict | None:
    """Finds medication info including price and calculated savings."""
    for key in ALTERNATIVE_KNOWLEDGE_BASE:
        if key in medication_name.lower():
            data = ALTERNATIVE_KNOWLEDGE_BASE[key]

            # Calculate savings for each alternative dynamically
            base_price = data.get("price_in_inr", 0)
            if base_price > 0:
                for alt in data.get("alternatives", []):
                    alt_price = alt.get("price_in_inr", 0)
                    savings = ((base_price - alt_price) / base_price) * 100
                    alt["savings_percentage"] = round(savings, 2)

            return data
    return None
