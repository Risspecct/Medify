def get_dataset_alt():

    ALTERNATIVE_KNOWLEDGE_BASE = {
    "paracetamol": {
        "description": "A common analgesic (pain reliever) and antipyretic (fever reducer) used for mild to moderate pain and fever.",
        "price_in_inr": 15,
        "alternatives": [
            {"name": "Ibuprofen", "price_in_inr": 20},
            {"name": "Aspirin", "price_in_inr": 10},
            {"name": "Naproxen", "price_in_inr": 110}
        ],
        "home_remedies_for_common_uses": {
            "For Fever": "Stay hydrated, rest, use a lukewarm compress.",
            "For Headache": "Rest in a quiet, dark room, apply a cold pack to the forehead, stay hydrated."
        },
        "notes": "Generally safe but can cause severe liver damage at very high doses. Do not exceed the recommended daily limit."
    },
    "ibuprofen": {
        "description": "A nonsteroidal anti-inflammatory drug (NSAID) used to relieve pain, fever, and inflammation.",
        "price_in_inr": 20,
        "alternatives": [
            {"name": "Paracetamol", "price_in_inr": 15},
            {"name": "Naproxen", "price_in_inr": 110}
        ],
        "home_remedies_for_common_uses": {
            "For Pain/Inflammation": "Rest the affected area, apply ice packs for the first 48 hours, then switch to heat."
        },
        "notes": "Should be taken with food to avoid stomach upset. Avoid if you have kidney problems or ulcers."
    },
    "cetirizine": {
        "description": "A second-generation antihistamine used to relieve allergy symptoms such as hay fever and hives.",
        "price_in_inr": 30,
        "alternatives": [
            {"name": "Loratadine", "price_in_inr": 80},
            {"name": "Fexofenadine", "price_in_inr": 160},
            {"name": "Chlorphenamine", "price_in_inr": 15}
        ],
        "home_remedies_for_common_uses": {
            "For Allergies": "Avoid known allergens, use a saline nasal rinse, keep windows closed during high pollen seasons."
        },
        "notes": "Classified as non-drowsy, but can still cause drowsiness in some individuals."
    },
    "amoxicillin": {
        "description": "A penicillin-type antibiotic used to treat a wide variety of bacterial infections.",
        "price_in_inr": 105,
        "alternatives": [
            {"name": "Doxycycline", "price_in_inr": 45},
            {"name": "Azithromycin", "price_in_inr": 125}
        ],
        "home_remedies_for_common_uses": {
            "General Support for Infections": "Get plenty of rest and stay hydrated. Take probiotics to help maintain gut health."
        },
        "notes": "Prescription-only. Complete the full course even if symptoms improve to prevent antibiotic resistance."
    },
    "naproxen": {
        "description": "A nonsteroidal anti-inflammatory drug (NSAID) used to relieve pain, inflammation, and stiffness.",
        "price_in_inr": 110,
        "alternatives": [
            {"name": "Ibuprofen", "price_in_inr": 20},
            {"name": "Paracetamol", "price_in_inr": 15}
        ],
        "home_remedies_for_common_uses": {
            "For Musculoskeletal Pain": "Rest, ice, compression, and elevation (RICE method). Gentle stretching.",
            "For Arthritis": "Low-impact exercise like swimming, applying heat or cold packs."
        },
        "notes": "Has a longer half-life than ibuprofen, allowing for less frequent dosing. Should be taken with food."
    },
    "loratadine": {
        "description": "A second-generation antihistamine used to relieve symptoms of allergic rhinitis (hay fever) and urticaria (hives).",
        "price_in_inr": 45,
        "alternatives": [
            {"name": "Cetirizine", "price_in_inr": 30},
            {"name": "Fexofenadine", "price_in_inr": 160}
        ],
        "home_remedies_for_common_uses": {
            "For Hay Fever": "Wear wraparound sunglasses, apply petroleum jelly around nostrils to trap pollen, and use a HEPA filter indoors."
        },
        "notes": "Classified as 'non-drowsy', though a small percentage of users may still experience sleepiness. Typically works within 1 to 3 hours."
    },
    "omeprazole": {
        "description": "A proton pump inhibitor (PPI) that reduces stomach acid. Used for GERD, heartburn, and ulcers.",
        "price_in_inr": 30,
        "alternatives": [
            {"name": "Pantoprazole", "price_in_inr": 80},
            {"name": "Rabeprazole", "price_in_inr": 100}
        ],
        "home_remedies_for_common_uses": {
            "For GERD/Heartburn": "Avoid trigger foods (spicy, fatty), eat smaller meals, and avoid lying down for 2-3 hours after eating."
        },
        "notes": "Must be taken on an empty stomach, 30-60 minutes before the first meal. Long-term use can lead to vitamin B-12 deficiency."
    },
    "atorvastatin": {
        "description": "A statin used to lower 'bad' cholesterol (LDL) and triglycerides while increasing 'good' cholesterol (HDL).",
        "price_in_inr": 56,
        "alternatives": [
            {"name": "Rosuvastatin", "price_in_inr": 120},
            {"name": "Simvastatin", "price_in_inr": 40}
        ],
        "home_remedies_for_common_uses": {
            "For High Cholesterol": "Adopt a low-fat diet (Mediterranean style), engage in regular aerobic exercise, and quit smoking."
        },
        "notes": "Avoid large quantities of grapefruit juice. Report any unexplained muscle pain or weakness to a doctor immediately."
    },
    "amlodipine": {
        "description": "A calcium channel blocker used for the treatment of hypertension (high blood pressure) and angina.",
        "price_in_inr": 25,
        "alternatives": [
            {"name": "Telmisartan", "price_in_inr": 60},
            {"name": "Cilnidipine", "price_in_inr": 80}
        ],
        "home_remedies_for_common_uses": {
            "For Hypertension": "Follow a low-sodium diet (DASH diet), maintain a healthy weight, and manage stress."
        },
        "notes": "Common side effect is swelling of the ankles (edema). Grapefruit juice can increase blood concentration levels."
    },
    "lisinopril": {
        "description": "An ACE inhibitor used to treat hypertension, manage heart failure, and improve survival after a heart attack.",
        "price_in_inr": 84,
        "alternatives": [
            {"name": "Enalapril", "price_in_inr": 30},
            {"name": "Ramipril", "price_in_inr": 50}
        ],
        "home_remedies_for_common_uses": {
            "For Hypertension": "Weight control, low-sodium diet, and regular physical activity are crucial alongside medication."
        },
        "notes": "A characteristic side effect is a dry, persistent cough. Contraindicated during pregnancy."
    },
    "sertraline": {
        "description": "An SSRI used to treat major depressive disorder, OCD, panic disorder, and social anxiety.",
        "price_in_inr": 75,
        "alternatives": [
            {"name": "Fluoxetine", "price_in_inr": 40},
            {"name": "Escitalopram", "price_in_inr": 90}
        ],
        "home_remedies_for_common_uses": {
            "For Mental Health": "Cognitive-behavioral therapy (CBT), regular exercise, and mindfulness meditation support treatment."
        },
        "notes": "Typically takes 4 to 6 weeks to reach full effect. Do not drink grapefruit juice while taking."
    },
    "fluoxetine": {
        "description": "An SSRI approved for the treatment of depression, OCD, bulimia nervosa, and panic disorder.",
        "price_in_inr": 40,
        "alternatives": [
            {"name": "Sertraline", "price_in_inr": 75},
            {"name": "Escitalopram", "price_in_inr": 90}
        ],
        "home_remedies_for_common_uses": {
            "For Mental Health": "Psychotherapy in combination with medication is often the most effective strategy. Avoid alcohol."
        },
        "notes": "Has a very long half-life, which reduces withdrawal severity but requires a long washout period if switching meds."
    },
    "alprazolam": {
        "description": "A fast-acting benzodiazepine used for short-term management of anxiety and panic disorders.",
        "price_in_inr": 74,
        "alternatives": [
            {"name": "Clonazepam", "price_in_inr": 60},
            {"name": "Etizolam", "price_in_inr": 80}
        ],
        "home_remedies_for_common_uses": {
            "For Anxiety": "Deep breathing exercises, progressive muscle relaxation, and avoiding caffeine or stimulants."
        },
        "notes": "High potential for addiction and physical dependence. Strictly prescription-only (Schedule X/H1 in India)."
    },
    "hydrocortisone_topical": {
        "description": "A low-potency topical steroid used for redness, swelling, and itching of skin conditions like eczema.",
        "price_in_inr": 42,
        "alternatives": [
            {"name": "Betamethasone", "price_in_inr": 25},
            {"name": "Clobetasol", "price_in_inr": 60}
        ],
        "home_remedies_for_common_uses": {
            "For Skin Conditions": "Avoid known irritants and keep skin moisturized with fragrance-free emollients."
        },
        "notes": "Do not apply to broken skin or infected areas. OTC use should not exceed 7 days."
    },
    "clotrimazole_topical": {
        "description": "An imidazole antifungal agent used to treat fungal skin infections such as athlete's foot, jock itch, and ringworm.",
        "price_in_inr": 45,
        "alternatives": [
            {"name": "Terbinafine", "price_in_inr": 120},
            {"name": "Luliconazole", "price_in_inr": 170},
            {"name": "Ketoconazole", "price_in_inr": 100}
        ],
        "home_remedies_for_common_uses": {
            "For Fungal Infections": "Keep the affected skin clean and dry, avoid tight-fitting synthetic clothing, and do not share towels."
        },
        "notes": "Treatment should be continued for the full duration (2-4 weeks) even if symptoms improve to prevent recurrence."
    },
    "mupirocin": {
        "description": "A topical antibiotic used for the treatment of impetigo and secondarily infected traumatic skin lesions like cuts.",
        "price_in_inr": 110,
        "alternatives": [
            {"name": "Neosporin Ointment", "price_in_inr": 60},
            {"name": "Povidone-Iodine", "price_in_inr": 45}
        ],
        "home_remedies_for_common_uses": {
            "For Skin Infections": "Keep the area clean and covered with a sterile bandage. Wash hands before and after application."
        },
        "notes": "Effective against MRSA. Complete the full course of treatment to prevent the development of antibiotic resistance."
    },
    "metformin": {
        "description": "A first-line oral medication used to improve glycemic control in people with type 2 diabetes.",
        "price_in_inr": 22,
        "alternatives": [
            {"name": "Glimepiride", "price_in_inr": 55},
            {"name": "Voglibose", "price_in_inr": 80}
        ],
        "home_remedies_for_common_uses": {
            "For Type 2 Diabetes": "A balanced diet focused on whole grains and lean proteins, combined with regular physical activity."
        },
        "notes": "Commonly causes gastrointestinal side effects like nausea. Should be taken with meals to minimize these effects."
    },
    "levothyroxine": {
        "description": "A synthetic thyroid hormone used as the standard treatment for hypothyroidism (underactive thyroid).",
        "price_in_inr": 168,
        "alternatives": [
            {"name": "Eltroxin", "price_in_inr": 210},
            {"name": "Thyronorm", "price_in_inr": 210}
        ],
        "home_remedies_for_common_uses": {
            "For Thyroid Health": "Ensure a balanced diet with adequate iodine (iodized salt, dairy, seafood). Manage stress and sleep."
        },
        "notes": "Must be taken on an empty stomach, 30-60 minutes before breakfast. Treatment is typically lifelong."
    },
    "insulin_glargine": {
        "description": "A long-acting insulin analog that provides a steady, peakless level of insulin over approximately 24 hours.",
        "price_in_inr": 650,
        "alternatives": [
            {"name": "Basalog", "price_in_inr": 570},
            {"name": "Glaritus", "price_in_inr": 640}
        ],
        "home_remedies_for_common_uses": {
            "For Diabetes Management": "Consistent blood glucose monitoring and a structured meal plan are essential."
        },
        "notes": "The primary risk is hypoglycemia. Injection sites should be rotated among the abdomen, thigh, and arm."
    },
    "salbutamol": {
        "description": "A rescue medication used for the rapid relief of bronchospasm in asthma and COPD.",
        "price_in_inr": 155,
        "alternatives": [
            {"name": "Levosalbutamol", "price_in_inr": 200},
            {"name": "Terbutaline", "price_in_inr": 40}
        ],
        "home_remedies_for_common_uses": {
            "For Asthma Management": "Identifying and avoiding triggers like pollen or dust. Practicing breathing exercises."
        },
        "notes": "Overuse (more than 3-4 times a week) suggests poor asthma control and requires a medical review."
    },
    "fluticasone": {
        "description": "A corticosteroid with potent anti-inflammatory activity. The nasal spray is used for allergic rhinitis (hay fever), and the topical cream is used for inflammatory skin conditions like eczema and psoriasis.",
        "price_in_inr": 372,
        "alternatives": [
            { "name": "Flomist-F Nasal Spray", "price_in_inr": 583 },
            { "name": "Flutizing Nasal Spray", "price_in_inr": 271 }
        ],
        "home_remedies_for_common_uses": {
            "For Allergies": "Avoiding known triggers and using saline nasal rinses.",
            "For Skin Conditions": "Using gentle, fragrance-free cleansers and regularly applying emollients to maintain the skin barrier."
        },
        "notes": "This is a controller medication, not for rescue. It must be used regularly to be effective. Rinse mouth after using the inhaler form to prevent oral thrush. Long-term use of high doses can have systemic effects."
    },
    "montelukast": {
        "description": "A leukotriene receptor antagonist used for the chronic treatment of asthma, prevention of exercise-induced bronchoconstriction, and relief of allergic rhinitis.",
        "price_in_inr": 142,
        "alternatives": [
            { "name": "Montecip LC (Montelukast + Levocetirizine)", "price_in_inr": 229 },
            { "name": "Leozet M", "price_in_inr": 47 }
        ],
        "home_remedies_for_common_uses": {
            "General Support for Asthma/Allergies": "Continue to use prescribed inhalers and have a rescue inhaler (like salbutamol) available at all times. Avoid known triggers."
        },
        "notes": "Carries an FDA boxed warning regarding the risk of serious neuropsychiatric events, including depression and suicidal thoughts. It is a controller medication and should not be used to treat an acute asthma attack."
    },
    "azithromycin": {
        "description": "A macrolide antibiotic used to treat a wide variety of bacterial infections, including chest infections, ear/nose/throat infections, skin infections, and certain STIs like chlamydia.",
        "price_in_inr": 125,
        "alternatives": [
            { "name": "Azicip 500", "price_in_inr": 75 },
            { "name": "Azee 500", "price_in_inr": 125 }
        ],
        "home_remedies_for_common_uses": {
            "General Support for Infections": "Complete the full course of antibiotics. Stay hydrated and get adequate rest. Taking probiotics may help mitigate gastrointestinal side effects like diarrhea."
        },
        "notes": "Associated with a risk of QT interval prolongation, which can lead to a potentially fatal heart rhythm disorder. Gastrointestinal side effects (diarrhea, nausea) are very common. Its long half-life allows for once-daily dosing and shorter treatment courses."
    },
    "ciprofloxacin": {
        "description": "A broad-spectrum fluoroquinolone antibiotic used to treat various bacterial infections, including urinary tract, respiratory, skin, and bone infections. Also used for anthrax exposure.",
        "price_in_inr": 45,
        "alternatives": [
            { "name": "Ciplox 500", "price_in_inr": 45 },
            { "name": "Cifran 500", "price_in_inr": 45 }
        ],
        "home_remedies_for_common_uses": {
            "General Support for Infections": "Drink plenty of liquids to stay hydrated. Complete the full course of treatment as prescribed to prevent resistance."
        },
        "notes": "Carries a boxed warning for serious side effects including tendonitis/tendon rupture, peripheral neuropathy (nerve damage), and central nervous system effects. Increases sensitivity to the sun. Avoid taking with dairy products or calcium-fortified juices."
    },
    "aspirin": {
        "description": "A nonsteroidal anti-inflammatory drug (NSAID) and antiplatelet agent used for pain, fever, inflammation, and to prevent blood clots, heart attacks, and strokes.",
        "price_in_inr": 5,
        "alternatives": [
            { "name": "Ecosprin 75", "price_in_inr": 6 },
            { "name": "Delisprin 75", "price_in_inr": 5 }
        ],
        "home_remedies_for_common_uses": {
            "For Pain": "Rest, application of cold or heat.",
            "For Cardiovascular Health": "A heart-healthy diet, regular exercise, and smoking cessation."
        },
        "notes": "Can cause stomach upset and bleeding. Should not be given to children or teenagers with viral infections due to the risk of Reye's syndrome."
    },
    "celecoxib": {
        "description": "A selective COX-2 inhibitor, a type of NSAID, used to treat arthritis, pain, and inflammation with a potentially lower risk of gastrointestinal side effects than traditional NSAIDs.",
        "price_in_inr": 316,
        "alternatives": [
            { "name": "Cobix 200", "price_in_inr": 145 },
            { "name": "Zycel 200", "price_in_inr": 316 }
        ],
        "home_remedies_for_common_uses": {
            "For Arthritis Pain": "Low-impact exercise, physical therapy, hot/cold therapy, maintaining a healthy weight."
        },
        "notes": "Prescription-only. Still carries a risk of cardiovascular events like heart attack and stroke. Should not be used in patients with a sulfa allergy."
    },
    "colchicine": {
        "description": "An anti-gout agent used to treat and prevent gout attacks. It works by reducing inflammation and the buildup of uric acid crystals in the joints.",
        "price_in_inr": 34,
        "alternatives": [
            { "name": "Goutnil 0.5", "price_in_inr": 34 },
            { "name": "Zycolchin 0.5", "price_in_inr": 29 }
        ],
        "home_remedies_for_common_uses": {
            "For Gout": "Avoid trigger foods high in purines (red meat, organ meats, certain seafood), limit alcohol (especially beer), stay hydrated, and rest the affected joint."
        },
        "notes": "Prescription-only. Can have significant gastrointestinal side effects (nausea, diarrhea). Has a narrow therapeutic window, and overdose can be very dangerous."
    },
    "cyclobenzaprine": {
        "description": "A skeletal muscle relaxant used for the short-term relief of muscle spasms and pain associated with acute musculoskeletal conditions.",
        "price_in_inr": 159,
        "alternatives": [
            { "name": "Skelebenz 10", "price_in_inr": 248 },
            { "name": "Mobrine", "price_in_inr": 196 }
        ],
        "home_remedies_for_common_uses": {
            "For Muscle Spasms": "Rest, ice/heat therapy, gentle stretching, and physical therapy."
        },
        "notes": "Prescription-only. A very common side effect is drowsiness, which can impair driving and other activities. Should only be used for short periods (2-3 weeks)."
    },
    "diclofenac": {
        "description": "A nonsteroidal anti-inflammatory drug (NSAID) used to treat pain, inflammation, and arthritis. Available in oral and topical forms.",
        "price_in_inr": 30,
        "alternatives": [
            { "name": "Voveran SR 100", "price_in_inr": 245 },
            { "name": "Reactin 50", "price_in_inr": 21 }
        ],
        "home_remedies_for_common_uses": {
            "For Pain/Inflammation": "Rest, ice, compression, elevation (RICE). Physical therapy."
        },
        "notes": "Available by prescription and in lower-strength topical forms over-the-counter. Carries similar risks of gastrointestinal and cardiovascular side effects as other NSAIDs."
    },
    "gabapentin": {
        "description": "An anticonvulsant medication also used to treat neuropathic (nerve) pain, such as postherpetic neuralgia (shingles pain) and diabetic neuropathy.",
        "price_in_inr": 153,
        "alternatives": [
            { "name": "Gabapin 300", "price_in_inr": 623 },
            { "name": "Pentanerv 300", "price_in_inr": 245 }
        ],
        "home_remedies_for_common_uses": {
            "For Nerve Pain": "Gentle exercise, physical therapy, mindfulness and meditation to manage the mental aspect of chronic pain, warm compresses."
        },
        "notes": "Prescription-only. Common side effects include dizziness and drowsiness. The dose is usually started low and increased gradually. Can have potential for misuse and dependence."
    },
    "meloxicam": {
        "description": "A nonsteroidal anti-inflammatory drug (NSAID) used to treat pain and inflammation from osteoarthritis and rheumatoid arthritis.",
        "price_in_inr": 87,
        "alternatives": [
            { "name": "Muvera 15", "price_in_inr": 149 },
            { "name": "Mobicam DT", "price_in_inr": 115 }
        ],
        "home_remedies_for_common_uses": {
            "For Arthritis": "Weight management, low-impact exercise, physical therapy, application of heat or cold."
        },
        "notes": "Prescription-only. It is longer-acting than ibuprofen, allowing for once-daily dosing. Carries the same cardiovascular and gastrointestinal risks as other NSAIDs."
    },
    "methocarbamol": {
        "description": "A central nervous system depressant used as a skeletal muscle relaxant to treat muscle spasms and pain.",
        "price_in_inr": 106,
        "alternatives": [
            { "name": "Robinax 500", "price_in_inr": 118 },
            { "name": "Robican 500", "price_in_inr": 106 }
        ],
        "home_remedies_for_common_uses": {
            "For Muscle Pain": "Rest, physical therapy, massage, and application of heat or ice."
        },
        "notes": "Prescription-only. Can cause drowsiness, dizziness, and lightheadedness. May turn urine brown, black, or green, which is a harmless side effect."
    },
    "oxycodone": {
        "description": "A potent opioid analgesic used for the management of moderate to severe pain.",
        "price_in_inr": 450,
        "alternatives": [
            { "name": "OxyContin (Global Brand)", "price_in_inr": 1200 },
            { "name": "Tapentadol (Often used as a clinical alternative in India)", "price_in_inr": 200 }
        ],
        "home_remedies_for_common_uses": {
            "For Pain Management": "Non-pharmacological approaches like physical therapy, acupuncture, massage, and cognitive-behavioral therapy can be used as part of a comprehensive pain management plan."
        },
        "notes": "Prescription-only, Schedule II/X controlled substance. High potential for addiction, abuse, and misuse. Side effects include constipation, drowsiness, and respiratory depression."
    },
    "prednisone": {
        "description": "A systemic corticosteroid used to treat a wide variety of inflammatory and autoimmune conditions, such as severe allergies, asthma, arthritis, and lupus.",
        "price_in_inr": 11,
        "alternatives": [
            { "name": "Wysolone 5", "price_in_inr": 11 },
            { "name": "Omnacortil 5", "price_in_inr": 7 }
        ],
        "home_remedies_for_common_uses": {
            "General Support for Inflammation": "An anti-inflammatory diet, stress management, and adequate rest can support overall health during treatment."
        },
        "notes": "Prescription-only. Long-term use can cause significant side effects, including weight gain, mood swings, osteoporosis, and increased risk of infection. The dose must be tapered off slowly, not stopped abruptly."
    },
    "pregabalin": {
        "description": "An anticonvulsant and gabapentinoid used to treat nerve pain, fibromyalgia, seizures, and generalized anxiety disorder.",
        "price_in_inr": 109,
        "alternatives": [
            { "name": "Pregalin 75", "price_in_inr": 212 },
            { "name": "Neugaba 75", "price_in_inr": 182 }
        ],
        "home_remedies_for_common_uses": {
            "For Nerve Pain/Fibromyalgia": "Graded exercise therapy, stress-reduction techniques like yoga and meditation, maintaining a regular sleep schedule."
        },
        "notes": "Prescription-only. Common side effects include dizziness, drowsiness, and weight gain. Can have potential for misuse and dependence."
    },
    "tizanidine": {
        "description": "A short-acting muscle relaxant (an alpha-2 adrenergic agonist) used to treat muscle spasticity.",
        "price_in_inr": 37,
        "alternatives": [
            { "name": "Tizan 2", "price_in_inr": 123 },
            { "name": "Tizpa 2", "price_in_inr": 34 }
        ],
        "home_remedies_for_common_uses": {
            "For Muscle Spasticity": "Stretching exercises, physical therapy, and occupational therapy."
        },
        "notes": "Prescription-only. Can cause significant drowsiness, dizziness, and dry mouth. It is short-acting and typically dosed multiple times per day."
    },
    "tramadol": {
        "description": "A centrally-acting opioid analgesic used to treat moderate to moderately severe pain.",
        "price_in_inr": 43,
        "alternatives": [
            { "name": "Tramazac 50", "price_in_inr": 51 },
            { "name": "Contramal 50", "price_in_inr": 103 }
        ],
        "home_remedies_for_common_uses": {
            "For Pain": "Physical therapy, ice/heat application, and mindfulness techniques can complement medication."
        },
        "notes": "Prescription-only, Schedule IV controlled substance. Carries a risk of addiction and dependence. Can lower the seizure threshold and has a risk of serotonin syndrome when combined with other serotonergic drugs."
    },
    "chlorphenamine": {
        "description": "A first-generation antihistamine used to relieve symptoms of allergies and the common cold.",
        "price_in_inr": 50,
        "alternatives": [
            { "name": "CPM 4", "price_in_inr": 85 },
            { "name": "Cadistin", "price_in_inr": 25 }
        ],
        "home_remedies_for_common_uses": {
            "For Cold/Allergy Symptoms": "Rest, hydration, saline nasal sprays, and using a humidifier."
        },
        "notes": "Commonly causes significant drowsiness and is often used in nighttime cold and allergy formulations. Anticholinergic side effects like dry mouth are also common."
    },
    "bismuth_subsalicylate": {
        "description": "An antidiarrheal and antacid used to treat diarrhea, heartburn, nausea, and upset stomach.",
        "price_in_inr": 250,
        "alternatives": [
            { "name": "Bismuth Subsalicylate (Generic)", "price_in_inr": 250 },
            { "name": "Pesto-Bismol (Imported)", "price_in_inr": 850 }
        ],
        "home_remedies_for_common_uses": {
            "For Diarrhea": "Stay hydrated with clear fluids or oral rehydration solutions. Follow the BRAT diet (bananas, rice, applesauce, toast)."
        },
        "notes": "Can cause a harmless darkening of the stool and tongue. Contains salicylate; should not be given to children or teenagers recovering from viral infections due to the risk of Reye's syndrome."
    },
    "esomeprazole": {
        "description": "A proton pump inhibitor (PPI) that reduces stomach acid. Used to treat GERD, ulcers, and other acid-related conditions.",
        "price_in_inr": 77,
        "alternatives": [
            { "name": "Nexpro 40", "price_in_inr": 165 },
            { "name": "Sompraz 40", "price_in_inr": 140 }
        ],
        "home_remedies_for_common_uses": {
            "For Acid Reflux": "Avoid trigger foods, eat smaller meals, don't lie down after eating, and elevate the head of the bed."
        },
        "notes": "Chemically very similar to omeprazole. Should be taken on an empty stomach before a meal. Long-term use carries risks like vitamin B12 deficiency and bone fractures."
    },
    "famotidine": {
        "description": "A histamine-2 (H2) blocker that reduces the amount of acid produced by the stomach. Used for GERD, ulcers, and heartburn.",
        "price_in_inr": 11,
        "alternatives": [
            { "name": "Famocid 20", "price_in_inr": 11 },
            { "name": "Facid 20", "price_in_inr": 8 }
        ],
        "home_remedies_for_common_uses": {
            "For Heartburn": "Dietary modifications, avoiding late-night meals, and weight management."
        },
        "notes": "Works faster than PPIs but is less potent and has a shorter duration of action. Available over-the-counter and by prescription."
    },
    "lansoprazole": {
        "description": "A proton pump inhibitor (PPI) used to treat and prevent stomach and intestinal ulcers, erosive esophagitis, and other conditions involving excessive stomach acid.",
        "price_in_inr": 65,
        "alternatives": [
            { "name": "Lanzol 30", "price_in_inr": 102 },
            { "name": "Junior Lanzol 15", "price_in_inr": 184 }
        ],
        "home_remedies_for_common_uses": {
            "For GERD": "Lifestyle changes such as diet modification, weight loss, and avoiding triggers."
        },
        "notes": "Should be taken before a meal. Long-term use is associated with an increased risk of bone fractures and vitamin B12 deficiency."
    },
    "loperamide": {
        "description": "An antidiarrheal agent used to decrease the frequency of diarrhea by slowing down intestinal movement.",
        "price_in_inr": 24,
        "alternatives": [
            { "name": "Lopamide", "price_in_inr": 25 },
            { "name": "Eldoper", "price_in_inr": 43 },
            { "name": "Roko", "price_in_inr": 26 }
        ],
        "home_remedies_for_common_uses": {
            "For Diarrhea": "Crucial to stay hydrated with water, broths, or oral rehydration solutions. The BRAT diet (bananas, rice, applesauce, toast) can help firm up stools."
        },
        "notes": "Should not be used if there is fever or bloody/black stool, as it can worsen certain infections. Overuse can lead to serious heart problems."
    },
    "metoclopramide": {
        "description": "A prokinetic agent and antiemetic used to treat GERD, nausea, and gastroparesis (delayed stomach emptying).",
        "price_in_inr": 14,
        "alternatives": [
            { "name": "Perinorm", "price_in_inr": 15 },
            { "name": "Vominorm", "price_in_inr": 12 },
            { "name": "Reglan", "price_in_inr": 10 }
        ],
        "home_remedies_for_common_uses": {
            "For Nausea/Gastroparesis": "Eating small, frequent meals that are low in fat and fiber. Avoiding carbonated beverages."
        },
        "notes": "Prescription-only. Carries a boxed warning for the risk of tardive dyskinesia (a serious, often irreversible movement disorder) with long-term or high-dose use."
    },
    "pantoprazole": {
        "description": "A proton pump inhibitor (PPI) that decreases the amount of acid produced in the stomach, used for GERD and erosive esophagitis.",
        "price_in_inr": 155,
        "alternatives": [
            { "name": "Pan 40", "price_in_inr": 175 },
            { "name": "Pantocid", "price_in_inr": 195 },
            { "name": "Pantop 40", "price_in_inr": 159 }
        ],
        "home_remedies_for_common_uses": {
            "For Acid Reflux": "Dietary and lifestyle adjustments, such as avoiding trigger foods and eating smaller meals."
        },
        "notes": "Prescription-only. Like other PPIs, it is associated with risks of bone fracture and vitamin B12 deficiency with long-term use."
    },
    "sucralfate": {
        "description": "A mucosal protectant used to treat and prevent ulcers. It works by forming a protective barrier over the ulcer against acid and enzymes.",
        "price_in_inr": 56,
        "alternatives": [
            { "name": "Sucrafil", "price_in_inr": 56 },
            { "name": "Sucramal", "price_in_inr": 49 }
        ],
        "home_remedies_for_common_uses": {
            "For Ulcers": "Avoid smoking, alcohol, and NSAIDs. Manage stress."
        },
        "notes": "Prescription-only. The most common side effect is constipation. It can interfere with the absorption of many other medications and should be taken at a different time."
    },
    "benazepril": {
        "description": "An angiotensin-converting enzyme (ACE) inhibitor used to treat high blood pressure and heart failure.",
        "price_in_inr": 85,
        "alternatives": [
            { "name": "Benace 5", "price_in_inr": 85 },
            { "name": "Aceptor 10", "price_in_inr": 120 }
        ],
        "home_remedies_for_common_uses": {
            "For Hypertension": "A low-sodium diet, regular exercise, and weight management."
        },
        "notes": "Prescription-only. Can cause a dry, persistent cough. Contraindicated in pregnancy."
    },
    "hydrochlorothiazide": {
        "description": "A thiazide diuretic ('water pill') used to treat high blood pressure and edema (fluid retention).",
        "price_in_inr": 11,
        "alternatives": [
            { "name": "Aquazide 12.5", "price_in_inr": 11 },
            { "name": "Hydrazide 25", "price_in_inr": 17 }
        ],
        "home_remedies_for_common_uses": {
            "For Edema/Hypertension": "Reducing sodium intake is very effective in conjunction with this medication."
        },
        "notes": "Prescription-only. Can cause increased urination and may affect potassium and sodium levels, requiring monitoring. Increases sun sensitivity."
    },
    "valsartan": {
        "description": "An angiotensin II receptor blocker (ARB) used to treat high blood pressure and heart failure.",
        "price_in_inr": 95,
        "alternatives": [
            { "name": "Valzaar 40", "price_in_inr": 95 },
            { "name": "Valent 160", "price_in_inr": 288 }
        ],
        "home_remedies_for_common_uses": {
            "For Hypertension": "Lifestyle modifications including diet (low sodium), exercise, and stress reduction."
        },
        "notes": "Prescription-only. Considered an alternative to ACE inhibitors for patients who cannot tolerate the cough. Contraindicated in pregnancy."
    },
    "glipizide": {
        "description": "A sulfonylurea drug used to control high blood sugar in people with type 2 diabetes. It works by stimulating the pancreas to release insulin.",
        "price_in_inr": 13,
        "alternatives": [
            { "name": "Glynase XL 5", "price_in_inr": 13 },
            { "name": "Glizid M (Combination with Metformin)", "price_in_inr": 112 }
        ],
        "home_remedies_for_common_uses": {
            "For Type 2 Diabetes": "Diet and exercise are essential components of management."
        },
        "notes": "Prescription-only. Carries a risk of hypoglycemia (low blood sugar). Can cause weight gain."
    },
    "glyburide": {
        "description": "A sulfonylurea drug used to treat type 2 diabetes by stimulating insulin release from the pancreas (known as Glibenclamide in India).",
        "price_in_inr": 10,
        "alternatives": [
            { "name": "Daonil 2.5", "price_in_inr": 4 },
            { "name": "Glinil-M (Glibenclamide + Metformin)", "price_in_inr": 22 }
        ],
        "home_remedies_for_common_uses": {
            "For Type 2 Diabetes": "A consistent diet and regular physical activity are crucial for blood sugar control."
        },
        "notes": "Prescription-only. Higher risk of hypoglycemia compared to some other diabetes medications. Can cause weight gain."
    },
    "liraglutide": {
        "description": "A GLP-1 receptor agonist, administered by injection, used to treat type 2 diabetes and, at a higher dose, for weight management.",
        "price_in_inr": 3500,
        "alternatives": [
            { "name": "Victoza (Novo Nordisk)", "price_in_inr": 3500 },
            { "name": "Lirafit (Glenmark)", "price_in_inr": 1600 }
        ],
        "home_remedies_for_common_uses": {
            "For Diabetes/Weight Management": "Must be used in conjunction with a reduced-calorie diet and increased physical activity."
        },
        "notes": "Prescription-only. Common side effects are gastrointestinal (nausea, diarrhea). Carries a boxed warning for the risk of thyroid C-cell tumors."
    },
    "semaglutide": {
        "description": "A GLP-1 receptor agonist used to treat type 2 diabetes and for chronic weight management. Available as a weekly injection or a daily oral tablet.",
        "price_in_inr": 3100,
        "alternatives": [
            { "name": "Rybelsus 3mg (Oral)", "price_in_inr": 2700 },
            { "name": "Wegovy 0.25mg (Injection)", "price_in_inr": 9500 },
            { "name": "Ozempic 0.25mg (Injection)", "price_in_inr": 10000 }
        ],
        "home_remedies_for_common_uses": {
            "For Diabetes/Weight Management": "A healthy diet and regular exercise are necessary for the medication to be effective."
        },
        "notes": "Prescription-only. Gastrointestinal side effects are common. Carries a boxed warning for the risk of thyroid C-cell tumors."
    },
    "sitagliptin": {
        "description": "A DPP-4 inhibitor used to treat type 2 diabetes. It works by increasing levels of incretin hormones, which help control blood sugar.",
        "price_in_inr": 105,
        "alternatives": [
            { "name": "Istavel 50", "price_in_inr": 105 },
            { "name": "Sitaxa 50", "price_in_inr": 193 },
            { "name": "Januvia 50", "price_in_inr": 222 }
        ],
        "home_remedies_for_common_uses": {
            "For Type 2 Diabetes": "Diet and exercise are fundamental to treatment."
        },
        "notes": "Prescription-only. Generally well-tolerated with a low risk of hypoglycemia. Has been associated with a risk of pancreatitis and severe joint pain."
    },
    "amitriptyline": {
        "description": "A tricyclic antidepressant (TCA) used to treat depression. It is also used off-label at lower doses for nerve pain and migraine prevention.",
        "price_in_inr": 25,
        "alternatives": [
            { "name": "Tryptomer 10", "price_in_inr": 76 },
            { "name": "Amitone 10", "price_in_inr": 20 },
            { "name": "Eliwel 10", "price_in_inr": 25 }
        ],
        "home_remedies_for_common_uses": {
            "For Depression/Pain": "Psychotherapy, exercise, and stress management techniques."
        },
        "notes": "Prescription-only. Has significant side effects, including drowsiness, dry mouth, and constipation, which are more pronounced than with newer antidepressants."
    },
    "aripiprazole": {
        "description": "An atypical antipsychotic used to treat schizophrenia, bipolar disorder, and as an add-on treatment for depression.",
        "price_in_inr": 95,
        "alternatives": [
            { "name": "Arpizol 5", "price_in_inr": 95 },
            { "name": "Asprito 5", "price_in_inr": 76 },
            { "name": "Aripiren 5", "price_in_inr": 54 }
        ],
        "home_remedies_for_common_uses": {
            "General Support for Mental Health": "Therapy, support groups, and a structured daily routine."
        },
        "notes": "Prescription-only. Carries a boxed warning for increased mortality in elderly patients with dementia-related psychosis and for suicidal thoughts in younger patients."
    },
    "bupropion": {
        "description": "An atypical antidepressant also used for smoking cessation. It works by affecting the neurotransmitters norepinephrine and dopamine.",
        "price_in_inr": 176,
        "alternatives": [
            { "name": "Bupron SR 150", "price_in_inr": 176 },
            { "name": "Zupion SR", "price_in_inr": 142 },
            { "name": "Bupep SR 150", "price_in_inr": 137 }
        ],
        "home_remedies_for_common_uses": {
            "For Depression": "Cognitive-behavioral therapy, exercise, and mindfulness.",
            "For Smoking Cessation": "Behavioral counseling and support groups."
        },
        "notes": "Prescription-only. Less likely to cause sexual side effects compared to SSRIs. Lowers the seizure threshold and should not be used in patients with a history of seizures or eating disorders."
    },
    "buspirone": {
        "description": "A non-benzodiazepine anxiolytic used for the treatment of generalized anxiety disorder (GAD).",
        "price_in_inr": 68,
        "alternatives": [
            { "name": "Buspin 10", "price_in_inr": 68 },
            { "name": "Buspinet 10", "price_in_inr": 36 },
            { "name": "Biziron 10", "price_in_inr": 50 }
        ],
        "home_remedies_for_common_uses": {
            "For Anxiety": "Therapy (CBT), meditation, deep breathing exercises, and regular physical activity."
        },
        "notes": "Prescription-only. Does not cause dependence or withdrawal like benzodiazepines, but it takes several weeks to become fully effective. Common side effects include dizziness and nausea."
    },
    "citalopram": {
        "description": "A selective serotonin reuptake inhibitor (SSRI) used to treat depression.",
        "price_in_inr": 85,
        "alternatives": [
            { "name": "Citalin 20", "price_in_inr": 85 },
            { "name": "Citopam 20", "price_in_inr": 72 },
            { "name": "Celepra 20", "price_in_inr": 94 }
        ],
        "home_remedies_for_common_uses": {
            "For Depression": "Psychotherapy, exercise, and maintaining a healthy lifestyle."
        },
        "notes": "Prescription-only. Carries a risk of dose-dependent QT prolongation (a heart rhythm issue), so doses are often limited, especially in older adults."
    },
    "clonazepam": {
        "description": "A long-acting benzodiazepine used to treat seizures, panic disorder, and anxiety.",
        "price_in_inr": 45,
        "alternatives": [
            { "name": "Clonotril 0.5", "price_in_inr": 52 },
            { "name": "Zapiz 0.5", "price_in_inr": 45 },
            { "name": "Petril 0.5", "price_in_inr": 58 }
        ],
        "home_remedies_for_common_uses": {
            "For Anxiety": "Stress management techniques and therapy."
        },
        "notes": "Prescription-only, Schedule IV/H1 controlled substance. Carries risks of dependence, tolerance, and withdrawal. Its long half-life can lead to next-day drowsiness."
    },
    "diazepam": {
        "description": "A long-acting benzodiazepine used to treat anxiety, seizures, muscle spasms, and symptoms of alcohol withdrawal.",
        "price_in_inr": 18,
        "alternatives": [
            { "name": "Calmpose 5", "price_in_inr": 18 },
            { "name": "Valium 5", "price_in_inr": 24 },
            { "name": "Placidox 5", "price_in_inr": 12 }
        ],
        "home_remedies_for_common_uses": {
            "For Anxiety/Muscle Spasms": "Relaxation techniques, physical therapy."
        },
        "notes": "Prescription-only, Schedule IV/H1 controlled substance. High potential for dependence. Long half-life can cause accumulation and prolonged sedation, especially in the elderly."
    },
    "duloxetine": {
        "description": "A serotonin-norepinephrine reuptake inhibitor (SNRI) used to treat depression, anxiety, nerve pain, and fibromyalgia.",
        "price_in_inr": 145,
        "alternatives": [
            { "name": "Duvanta 20", "price_in_inr": 145 },
            { "name": "Symbal 20", "price_in_inr": 158 },
            { "name": "Delok 20", "price_in_inr": 112 }
        ],
        "home_remedies_for_common_uses": {
            "For Depression/Pain": "A combination of medication with therapy, physical activity, and stress reduction is most effective."
        },
        "notes": "Prescription-only. Can cause nausea, dry mouth, and fatigue. Discontinuation should be done gradually to avoid withdrawal symptoms."
    },
    "escitalopram": {
        "description": "A selective serotonin reuptake inhibitor (SSRI) used to treat depression and generalized anxiety disorder.",
        "price_in_inr": 95,
        "alternatives": [
            { "name": "Nexito 10", "price_in_inr": 105 },
            { "name": "Cilentra 10", "price_in_inr": 95 },
            { "name": "Stalopam 10", "price_in_inr": 110 }
        ],
        "home_remedies_for_common_uses": {
            "For Depression/Anxiety": "Therapy (CBT), mindfulness, exercise, and a stable routine."
        },
        "notes": "Prescription-only. Often considered to have fewer side effects than other SSRIs. Like others in its class, it can take several weeks to work fully."
    },
    "lamotrigine": {
        "description": "An anticonvulsant medication also used as a mood stabilizer in bipolar disorder.",
        "price_in_inr": 185,
        "alternatives": [
            { "name": "Lamictal 50", "price_in_inr": 245 },
            { "name": "Lametec DT 50", "price_in_inr": 185 },
            { "name": "Lamoset 50", "price_in_inr": 156 }
        ],
        "home_remedies_for_common_uses": {
            "General Support for Bipolar/Epilepsy": "Maintaining a regular sleep schedule, managing stress, and avoiding alcohol."
        },
        "notes": "Prescription-only. Requires a very slow dose titration when starting to reduce the risk of a serious, potentially life-threatening skin rash (Stevens-Johnson syndrome)."
    },
    "levetiracetam": {
        "description": "An anticonvulsant medication used to treat various types of seizures.",
        "price_in_inr": 138,
        "alternatives": [
            { "name": "Levipil 500", "price_in_inr": 145 },
            { "name": "Keppra 500", "price_in_inr": 750 },
            { "name": "Levera 500", "price_in_inr": 138 }
        ],
        "home_remedies_for_common_uses": {
            "For Epilepsy": "Ensuring adequate sleep, managing stress, and avoiding known seizure triggers."
        },
        "notes": "Prescription-only. Generally well-tolerated but can cause behavioral side effects like irritability, agitation, and mood swings."
    },
    "lorazepam": {
        "description": "An intermediate-acting benzodiazepine used to treat anxiety, insomnia, and seizures.",
        "price_in_inr": 35,
        "alternatives": [
            { "name": "Ativan 1", "price_in_inr": 42 },
            { "name": "Larpose 1", "price_in_inr": 35 },
            { "name": "Lopez 1", "price_in_inr": 28 }
        ],
        "home_remedies_for_common_uses": {
            "For Anxiety/Insomnia": "Cognitive-behavioral therapy for insomnia (CBT-I), relaxation techniques, and good sleep hygiene."
        },
        "notes": "Prescription-only, Schedule IV/H1 controlled substance. Carries risks of dependence, tolerance, and withdrawal. Often used in hospital settings for sedation."
    },
    "olanzapine": {
        "description": "An atypical antipsychotic used to treat schizophrenia and bipolar disorder.",
        "price_in_inr": 62,
        "alternatives": [
            { "name": "Oleanz 5", "price_in_inr": 75 },
            { "name": "Olan 5", "price_in_inr": 62 },
            { "name": "Joyゾー (Joyzo) 5", "price_in_inr": 55 }
        ],
        "home_remedies_for_common_uses": {
            "General Support for Mental Health": "A supportive environment, therapy, and a consistent daily routine."
        },
        "notes": "Prescription-only. Associated with significant metabolic side effects, including weight gain, high blood sugar, and high cholesterol."
    },
    "topiramate": {
        "description": "An anticonvulsant medication also used for migraine prevention and sometimes for weight loss in combination with another drug.",
        "price_in_inr": 124,
        "alternatives": [
            { "name": "Topaz 25", "price_in_inr": 135 },
            { "name": "Topirol 25", "price_in_inr": 124 },
            { "name": "Topamac 25", "price_in_inr": 160 }
        ],
        "home_remedies_for_common_uses": {
            "For Migraines": "Identifying and avoiding triggers, maintaining a regular sleep and meal schedule, and stress management."
        },
        "notes": "Prescription-only. Common side effects include cognitive issues ('brain fog'), tingling in extremities, and kidney stones. Requires slow dose titration."
    },
    "bacitracin": {
        "description": "A polypeptide antibiotic used topically to prevent minor skin infections in cuts, scrapes, and burns.",
        "price_in_inr": 95,
        "alternatives": [
            { "name": "Bacitracin Ointment (Generic)", "price_in_inr": 95 },
            { "name": "Neosporin (Triple Antibiotic)", "price_in_inr": 115 }
        ],
        "home_remedies_for_common_uses": {
            "For Minor Wounds": "Clean the wound thoroughly with soap and water, apply the antibiotic, and cover with a sterile bandage."
        },
        "notes": "Available over-the-counter. Contact dermatitis (allergic skin reaction) is a potential side effect."
    },
    "cephalexin": {
        "description": "A first-generation cephalosporin antibiotic used to treat a variety of bacterial infections, particularly skin and soft tissue infections.",
        "price_in_inr": 115,
        "alternatives": [
            { "name": "Phexin 500", "price_in_inr": 155 },
            { "name": "Ceff 500", "price_in_inr": 115 },
            { "name": "Sporidex 500", "price_in_inr": 195 }
        ],
        "home_remedies_for_common_uses": {
            "General Support for Infections": "Rest, hydration, and completing the full course of medication."
        },
        "notes": "Prescription-only. Generally well-tolerated. Patients with a severe penicillin allergy may also be allergic to cephalosporins."
    },
    "clindamycin": {
        "description": "A lincosamide antibiotic used to treat a wide range of serious bacterial infections, including skin, lung, and internal organ infections.",
        "price_in_inr": 215,
        "alternatives": [
            { "name": "Dalacin C 300", "price_in_inr": 485 },
            { "name": "Clindac 300", "price_in_inr": 215 },
            { "name": "Cleocin (Global Brand)", "price_in_inr": 950 }
        ],
        "home_remedies_for_common_uses": {
            "General Support for Infections": "Adequate rest and fluid intake."
        },
        "notes": "Prescription-only. Carries a boxed warning for a high risk of causing C. difficile-associated diarrhea, which can be severe."
    },
    "doxycycline": {
        "description": "A tetracycline antibiotic used to treat bacterial infections, malaria, acne, and rosacea.",
        "price_in_inr": 24,
        "alternatives": [
            { "name": "Doxy-1 LDR", "price_in_inr": 115 },
            { "name": "Doxivital", "price_in_inr": 24 },
            { "name": "Tetradox", "price_in_inr": 48 }
        ],
        "home_remedies_for_common_uses": {
            "For Acne": "A consistent skincare routine with gentle cleansers and non-comedogenic moisturizers."
        },
        "notes": "Prescription-only. Should be taken with a full glass of water. Causes significant sun sensitivity. Not recommended for children under 8."
    },
    "metronidazole": {
        "description": "A nitroimidazole antibiotic and antiprotozoal used to treat bacterial and protozoal infections.",
        "price_in_inr": 15,
        "alternatives": [
            { "name": "Flagyl 400", "price_in_inr": 22 },
            { "name": "Metrogyl 400", "price_in_inr": 15 },
            { "name": "Aristogyl 400", "price_in_inr": 12 }
        ],
        "home_remedies_for_common_uses": {
            "General Support for Infections": "Completing the full course of medication."
        },
        "notes": "Prescription-only. Alcohol must be strictly avoided during treatment and for 3 days after. Can cause a metallic taste."
    },
    "terbinafine": {
        "description": "An allylamine antifungal used to treat fungal infections of the skin and nails.",
        "price_in_inr": 285,
        "alternatives": [
            { "name": "Sebifin 250", "price_in_inr": 315 },
            { "name": "Terbiforce 250", "price_in_inr": 285 },
            { "name": "Tyza 250", "price_in_inr": 250 }
        ],
        "home_remedies_for_common_uses": {
            "For Fungal Infections": "Keep skin clean and dry, wear breathable footwear."
        },
        "notes": "Oral terbinafine can cause liver problems and requires monitoring. It can also cause disturbances in taste and smell."
    }
}

    return ALTERNATIVE_KNOWLEDGE_BASE