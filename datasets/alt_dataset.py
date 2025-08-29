def get_dataset_alt():
    ALTERNATIVE_KNOWLEDGE_BASE = {
        "paracetamol": {
            "description": "A common pain reliever and fever reducer.",
            "alternatives": [
                "Ibuprofen (also an anti-inflammatory, but check for stomach issues)",
                "Aspirin (not for children, also a blood thinner)"
            ],
            "home_remedies_for_common_uses": {
                "For Fever": "Stay hydrated, rest, use a lukewarm compress.",
                "For Headache": "Rest in a quiet room, apply a cold pack, stay hydrated."
            },
            "notes": "Paracetamol is generally safe but can cause liver damage at very high doses."
        },
        "ibuprofen": {
            "description": "A nonsteroidal anti-inflammatory drug (NSAID) for pain, fever, and inflammation.",
            "alternatives": [
                "Paracetamol (safer for the stomach but not anti-inflammatory)",
                "Naproxen (another NSAID, longer-lasting)"
            ],
            "home_remedies_for_common_uses": {
                "For Pain/Inflammation": "Rest the affected area, apply ice packs.",
            },
            "notes": "Should be taken with food to avoid stomach upset. Avoid if you have kidney problems or ulcers."
        },
        "cetirizine": {
            "description": "An antihistamine used to relieve allergy symptoms.",
            "alternatives": [
                "Loratadine (less likely to cause drowsiness)",
                "Fexofenadine (also a non-drowsy option)"
            ],
            "home_remedies_for_common_uses": {
                "For Allergies": "Avoid known allergens, use a saline nasal rinse, keep windows closed during high pollen seasons."
            },
            "notes": "Can cause drowsiness in some individuals."
        },
        "amoxicillin": {
            "description": "A penicillin-type antibiotic used to treat bacterial infections.",
            "alternatives": [
                "Doxycycline (for patients with penicillin allergy)",
                "Azithromycin (another common alternative for respiratory infections)"
            ],
            "home_remedies_for_common_uses": {
                "General Support for Infections": "Get plenty of rest, stay hydrated to help your body fight the infection."
            },
            "notes": "This is a prescription-only medication. Alternatives must be prescribed by a doctor."
        }
    }
    return ALTERNATIVE_KNOWLEDGE_BASE