def get_dataset():
    medications = [
        "aspirin", "amoxicillin", "paracetamol", "ibuprofen", "lisinopril", "ondansetron",
        "omeprazole", "atorvastatin", "warfarin", "albuterol", "metformin", "azithromycin",
        "doxycycline", "ceftriaxone", "cetirizine", "pantoprosole", "levocetirizine",
        "domperidone", "diclofenac", "losartan", "amlodipine", "montelukast", "clopidogrel",
        "zoloft", "cough syrup", "dolo 650", "crocin", "calpol", "combiflam", "meftal p",
        "meftal spas", "okacet", "alerid", "azee", "levolin", "betadine", "sinarest",
        "asthalin", "ventolin", "thyronorm", "ecosprin", "shelcal", "becosules", "revital"
    ]

    symptoms = [
        "fever", "headache", "chest pain", "sore throat", "cold", "cough", "stomach pain",
        "vomiting", "loose motion", "diarrhea", "acidity", "gas", "heartburn", "nausea",
        "fatigue", "weakness", "shortness of breath", "migraine", "jaundice", "malaria",
        "dengue", "high blood pressure", "diabetes", "anxiety", "high cholesterol",
        "flu symptoms", "body aches", "dizzy"
    ]

    dosage_units = [
        "mg", "g", "ml", "mcg", "units", "puffs", "drops", "sachets",
        "tablet", "tablets", "capsule", "capsules", "pill", "pills",
        "injection", "injections", "ampoule", "vial"
    ]

    frequencies = [
        "daily", "once a day", "twice a day", "three times a day", "four times a day",
        "od", "bid", "tds", "qid", "hs", "prn", "as needed", "stat", "immediately",
        "every morning", "every evening", "before breakfast", "after meals", "at bedtime",
        r'every\s*(\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)\s*hours'
    ]
    return medications, symptoms, dosage_units, frequencies
