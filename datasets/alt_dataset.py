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
                "For Pain/Inflammation": "Rest the affected area, apply ice packs."
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
        },
        "paracetamol": {
            "description": "A common analgesic (pain reliever) and antipyretic (fever reducer) used for mild to moderate pain and fever.",
            "alternatives": [
                "Ibuprofen (also an anti-inflammatory, but check for stomach issues)",
                "Aspirin (not for children, also a blood thinner)",
                "Naproxen"
            ],
            "home_remedies_for_common_uses": {
                "For Fever": "Stay hydrated, rest, use a lukewarm compress.",
                "For Headache": "Rest in a quiet, dark room, apply a cold pack to the forehead, stay hydrated."
            },
            "notes": "Generally safe but can cause severe liver damage at very high doses. It is important not to exceed the recommended daily limit."
        },
        "ibuprofen": {
            "description": "A nonsteroidal anti-inflammatory drug (NSAID) used to relieve pain, fever, and inflammation.",
            "alternatives": [],
            "home_remedies_for_common_uses": {
                "For Pain/Inflammation": "Rest the affected area, apply ice packs for the first 48 hours, then switch to heat."
            },
            "notes": "Should be taken with food to avoid stomach upset. Long-term use can increase the risk of heart attack, stroke, and stomach bleeding. Avoid if you have kidney problems or ulcers."
        },
        "cetirizine": {
            "description": "A second-generation antihistamine used to relieve allergy symptoms such as hay fever and hives.",
            "alternatives": [
                "Loratadine (less likely to cause drowsiness)",
                "Fexofenadine (also a non-drowsy option)",
                "Chlorphenamine (first-generation, can cause more drowsiness)"
            ],
            "home_remedies_for_common_uses": {
                "For Allergies": "Avoid known allergens, use a saline nasal rinse, keep windows closed during high pollen seasons, wash hair and clothes after being outside."
            },
            "notes": "Classified as non-drowsy, but can still cause drowsiness in some individuals. Generally starts working within an hour."
        },
        "amoxicillin": {
            "description": "A penicillin-type antibiotic used to treat a wide variety of bacterial infections.",
            "alternatives": [],
            "home_remedies_for_common_uses": {
                "General Support for Infections": "Get plenty of rest and stay hydrated to help your body fight the infection. Take probiotics to help maintain gut health."
            },
            "notes": "This is a prescription-only medication. It is crucial to complete the full course as prescribed, even if symptoms improve, to prevent antibiotic resistance. Not effective against viral infections like the common cold or flu."
        },
        "naproxen": {
            "description": "A nonsteroidal anti-inflammatory drug (NSAID) used to relieve pain, inflammation, and stiffness associated with conditions like arthritis, gout, and menstrual cramps.",
            "alternatives": [],
            "home_remedies_for_common_uses": {
                "For Musculoskeletal Pain": "Rest, ice, compression, and elevation (RICE method) for injuries like sprains. Gentle stretching and physical therapy exercises.",
                "For Arthritis": "Low-impact exercise like swimming or walking, applying heat or cold packs to affected joints, maintaining a healthy weight."
            },
            "notes": "Has a longer half-life than ibuprofen, allowing for less frequent dosing. Carries a risk of serious gastrointestinal bleeding, heart attack, and stroke, particularly with long-term use. Should be taken with food."
        },
        "loratadine": {
            "description": "A second-generation antihistamine used to relieve symptoms of allergic rhinitis (hay fever) and urticaria (hives), such as sneezing, runny nose, and itching.",
            "alternatives": [],
            "home_remedies_for_common_uses": {
                "For Hay Fever": "Wear wraparound sunglasses, apply petroleum jelly around nostrils to trap pollen, shower after being outdoors, keep windows closed, and use a HEPA filter indoors."
            },
            "notes": "Classified as 'non-drowsy' as it does not readily cross the blood-brain barrier, but a small percentage of users may still experience sleepiness. Typically begins to work within 1 to 3 hours."
        },
        "omeprazole": {
            "description": "A proton pump inhibitor (PPI) that reduces the amount of acid produced in the stomach. Used to treat GERD, heartburn, and stomach ulcers.",
            "alternatives": [],
            "home_remedies_for_common_uses": {
                "For GERD/Heartburn": "Avoid trigger foods (e.g., spicy, fatty, acidic), eat smaller meals, avoid lying down for 2-3 hours after eating, elevate the head of the bed, and manage weight."
            },
            "notes": "For maximum efficacy, it must be taken on an empty stomach, 30-60 minutes before the first meal of the day. Long-term use can lead to vitamin B-12 deficiency and an increased risk of bone fractures."
        },
        "atorvastatin": {
            "description": "An HMG-CoA reductase inhibitor (statin) used to lower levels of 'bad' cholesterol (LDL) and triglycerides, while increasing 'good' cholesterol (HDL). It is used to reduce the risk of heart attack and stroke.",
            "alternatives":[],
            "home_remedies_for_common_uses": {
                "For High Cholesterol": "Adopt a low-fat, low-cholesterol diet (like the Mediterranean diet), engage in regular aerobic exercise, maintain a healthy weight, and quit smoking."
            },
            "notes": "Avoid consuming large quantities of grapefruit or grapefruit juice. Report any unexplained muscle pain, tenderness, or weakness immediately, as this could be a sign of a rare but serious condition called rhabdomyolysis."
        },
        "amlodipine": {
            "description": "A calcium channel blocker used for the treatment of hypertension (high blood pressure) and to treat and prevent angina (chest pain).",
            "alternatives":[],
            "home_remedies_for_common_uses": {
                "For Hypertension": "Follow a low-sodium diet (like the DASH diet), maintain a healthy weight, exercise regularly, limit alcohol consumption, and manage stress."
            },
            "notes": "The most common side effect is swelling of the hands, feet, or ankles (peripheral edema). Consuming large amounts of grapefruit or grapefruit juice can increase the concentration of amlodipine in the blood and worsen side effects."
        },
        "lisinopril": {
            "description": "An angiotensin-converting enzyme (ACE) inhibitor used to treat hypertension (high blood pressure), manage heart failure, and improve survival after a heart attack.",
            "alternatives":[],
            "home_remedies_for_common_uses": {
                "For Hypertension": "Weight control, a low-sodium diet, regular physical activity, and limiting alcohol intake are crucial alongside medication."
            },
            "notes": "The most characteristic side effect is a dry, tickly, persistent cough. The first dose may cause significant dizziness and is often recommended to be taken at bedtime. Contraindicated during pregnancy due to risk of fetal harm."
        },
        "sertraline": {
            "description": "A selective serotonin reuptake inhibitor (SSRI) used to treat major depressive disorder (MDD), obsessive-compulsive disorder (OCD), panic disorder, PTSD, and social anxiety disorder.",
            "alternatives":[],
            "home_remedies_for_common_uses": {
                "For Mental Health Conditions": "Cognitive-behavioral therapy (CBT), regular exercise, mindfulness meditation, maintaining a consistent sleep schedule, and a balanced diet can support treatment."
            },
            "notes": "Carries a warning for an increased risk of suicidal thoughts and behaviors in children and young adults. It typically takes 4 to 6 weeks to reach its full therapeutic effect. Do not drink grapefruit juice while taking."
        },
        "fluoxetine": {
             "description": "A selective serotonin reuptake inhibitor (SSRI) approved for the treatment of major depressive disorder (MDD), obsessive-compulsive disorder (OCD), bulimia nervosa, and panic disorder.",
            "alternatives":[],
            "home_remedies_for_common_uses": {
                "For Mental Health Conditions": "Psychotherapy (talk therapy) in combination with medication is often the most effective treatment strategy. Regular physical activity and stress management techniques are also beneficial."
            },
            "notes": "Has a very long elimination half-life, which reduces the severity of withdrawal symptoms but requires a long 'washout' period when switching to other interacting medications like MAOIs. Avoid alcohol."
        },
        "alprazolam": {
            "description": "A fast-acting benzodiazepine used for the short-term management of anxiety disorders and for the treatment of panic disorder.",
            "alternatives":[],
            "home_remedies_for_common_uses": {
                "For Anxiety": "Deep breathing exercises, mindfulness meditation, progressive muscle relaxation, regular exercise, and avoiding caffeine and other stimulants."
            },
            "notes": "High potential for abuse, misuse, and addiction. Can cause physical dependence and severe withdrawal symptoms. Co-administration with opioids or other CNS depressants (including alcohol) can result in profound sedation, respiratory depression, coma, and death. Grapefruit and grapefruit juice should not be consumed."
        },
        "hydrocortisone_topical": {
            "description": "A low-potency topical corticosteroid used to treat the redness, swelling, itching, and discomfort of various inflammatory skin conditions like eczema, dermatitis, and insect bites.",
            "alternatives": [
                "More potent topical steroids (prescription-only, for severe conditions)",
                "Non-steroidal creams or emollients (for mild inflammation)",
                "Calcineurin inhibitors (e.g., tacrolimus, for sensitive areas)"
            ],
            "home_remedies_for_common_uses": {
            "For Skin Conditions": "Avoiding known irritants and allergens, keeping the skin well-moisturized with fragrance-free emollients, and taking lukewarm baths with colloidal oatmeal."
        },
        "notes": "Should not be applied to broken skin, cuts, or infected areas. Long-term or extensive use can lead to skin thinning (atrophy). Over-the-counter use should not exceed 7 days without consulting a doctor."
    },
    "clotrimazole_topical": {
        "description": "An imidazole antifungal agent used to treat fungal skin infections such as athlete's foot (tinea pedis), jock itch (tinea cruris), and ringworm (tinea corporis).",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Fungal Infections": "Keep the affected skin clean and dry, avoid tight-fitting synthetic clothing (wear loose cotton instead), and do not share towels. For athlete's foot, dry thoroughly between the toes and wear clean, changed-daily cotton socks."
        },
        "notes": "Treatment should be continued for the full recommended duration (e.g., 2-4 weeks) even if symptoms improve earlier to prevent recurrence. The cream form can damage latex condoms and diaphragms, reducing their effectiveness."
    },
    "mupirocin": {
        "description": "A topical antibiotic used for the treatment of impetigo and secondarily infected traumatic skin lesions (e.g., infected cuts or wounds).",
        "alternatives": [
            "Over-the-counter antibiotic ointments (e.g., Neosporin, bacitracin) for prevention in minor cuts.",
            "Oral antibiotics (Cephalexin, Clindamycin) for more severe or widespread infections."
        ],
        "home_remedies_for_common_uses": {
            "For Skin Infections": "Keep the area clean and covered with a sterile bandage. Wash hands before and after application to prevent spreading the infection."
        },
        "notes": "Effective against methicillin-resistant Staphylococcus aureus (MRSA). It is important to complete the full course of treatment to prevent recurrence and the development of antibiotic resistance. Contact a healthcare provider if there is no improvement after 3 to 5 days."
    },
    "metformin": {
        "description": "A first-line biguanide oral medication used to improve glycemic control in people with type 2 diabetes. It is also used off-label for polycystic ovary syndrome (PCOS).",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Type 2 Diabetes": "A cornerstone of treatment is a balanced diet focused on whole grains, lean proteins, and vegetables, combined with regular physical activity and weight management."
        },
        "notes": "Carries a boxed warning for a rare but serious condition called lactic acidosis. Gastrointestinal side effects (diarrhea, nausea) are very common, especially when starting. Should be taken with meals to minimize these effects. Excessive alcohol intake increases the risk of lactic acidosis."
    },
    "levothyroxine": {
        "description": "A synthetic thyroid hormone used as the standard treatment for hypothyroidism (underactive thyroid) and as an adjunctive therapy for certain types of thyroid cancer.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Thyroid Health": "A balanced diet with adequate iodine is necessary for natural thyroid function. Foods rich in iodine include iodized salt, dairy products, seafood, and eggs. Manage stress and ensure adequate sleep."
        },
        "notes": "Must be taken once daily on an empty stomach, 30 to 60 minutes before breakfast, with a full glass of water. Has a narrow therapeutic index; the dose must be carefully monitored with regular blood tests. Treatment is typically lifelong."
    },
    "insulin_glargine": {
        "description": "A long-acting insulin analog used to improve glycemic control in people with type 1 and type 2 diabetes. It provides a steady, peakless, basal (background) level of insulin over approximately 24 hours.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Diabetes Management": "A structured meal plan, regular physical activity, and consistent blood glucose monitoring are essential. Patients should be educated on how to recognize and treat hypoglycemia with a quick-acting source of sugar."
        },
        "notes": "The most significant risk is hypoglycemia (low blood sugar). Injection sites should be rotated among the abdomen, thigh, and upper arm to prevent lipodystrophy (changes in fatty tissue). Must not be mixed with any other insulin in the same syringe."
    },
    "salbutamol": {
        "description": "A short-acting beta-2 agonist (SABA) bronchodilator, also known as Albuterol. It is used as a 'reliever' or 'rescue' medication for the rapid relief of bronchospasm in asthma and COPD.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Asthma Management": "Identifying and avoiding triggers (pollen, dust mites, pet dander). Using allergy-proof bedding and removing carpets can help reduce exposure to indoor allergens. Practicing breathing exercises."
        },
        "notes": "Common side effects include shakiness (tremor), nervousness, and a fast heart rate. Overuse (more than 3-4 times a week) can be a sign of worsening asthma control and requires medical review. Proper inhaler technique is critical for effectiveness."
    },
    "fluticasone": {
        "description": "A corticosteroid with potent anti-inflammatory activity. The nasal spray is used for allergic rhinitis (hay fever), and the topical cream is used for inflammatory skin conditions like eczema and psoriasis.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Allergies": "Avoiding known triggers and using saline nasal rinses.",
            "For Skin Conditions": "Using gentle, fragrance-free cleansers and regularly applying emollients to maintain the skin barrier."
        },
        "notes": "This is a controller medication, not for rescue. It must be used regularly to be effective. Rinse mouth after using the inhaler form to prevent oral thrush. Long-term use of high doses can have systemic effects."
    },
    "montelukast": {
        "description": "A leukotriene receptor antagonist used for the chronic treatment of asthma, prevention of exercise-induced bronchoconstriction, and relief of allergic rhinitis.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "General Support for Asthma/Allergies": "Continue to use prescribed inhalers and have a rescue inhaler (like salbutamol) available at all times. Avoid known triggers."
        },
        "notes": "Carries an FDA boxed warning regarding the risk of serious neuropsychiatric events, including depression and suicidal thoughts. It is a controller medication and should not be used to treat an acute asthma attack."
    },
    "azithromycin": {
        "description": "A macrolide antibiotic used to treat a wide variety of bacterial infections, including chest infections, ear/nose/throat infections, skin infections, and certain STIs like chlamydia.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "General Support for Infections": "Complete the full course of antibiotics. Stay hydrated and get adequate rest. Taking probiotics may help mitigate gastrointestinal side effects like diarrhea."
        },
        "notes": "Associated with a risk of QT interval prolongation, which can lead to a potentially fatal heart rhythm disorder. Gastrointestinal side effects (diarrhea, nausea) are very common. Its long half-life allows for once-daily dosing and shorter treatment courses."
    },
    "ciprofloxacin": {
        "description": "A broad-spectrum fluoroquinolone antibiotic used to treat various bacterial infections, including urinary tract, respiratory, skin, and bone infections. Also used for anthrax exposure.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "General Support for Infections": "Drink plenty of liquids to stay hydrated. Complete the full course of treatment as prescribed to prevent resistance."
        },
        "notes": "Carries a boxed warning for serious side effects including tendonitis/tendon rupture, peripheral neuropathy (nerve damage), and central nervous system effects. Increases sensitivity to the sun. Avoid taking with dairy products or calcium-fortified juices."
    },
    "aspirin": {
        "description": "A nonsteroidal anti-inflammatory drug (NSAID) and antiplatelet agent used for pain, fever, inflammation, and to prevent blood clots, heart attacks, and strokes.",
        "alternatives": [
            "Ibuprofen (for pain/fever)",
            "Acetaminophen (for pain/fever, not anti-inflammatory)",
            "Clopidogrel (as an antiplatelet alternative)"
        ],
        "home_remedies_for_common_uses": {
            "For Pain": "Rest, application of cold or heat.",
            "For Cardiovascular Health": "A heart-healthy diet, regular exercise, and smoking cessation."
        },
        "notes": "Can cause stomach upset and bleeding. Should not be given to children or teenagers with viral infections due to the risk of Reye's syndrome."
    },
    "celecoxib": {
        "description": "A selective COX-2 inhibitor, a type of NSAID, used to treat arthritis, pain, and inflammation with a potentially lower risk of gastrointestinal side effects than traditional NSAIDs.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Arthritis Pain": "Low-impact exercise, physical therapy, hot/cold therapy, maintaining a healthy weight."
        },
        "notes": "Prescription-only. Still carries a risk of cardiovascular events like heart attack and stroke. Should not be used in patients with a sulfa allergy."
    },
    "colchicine": {
        "description": "An anti-gout agent used to treat and prevent gout attacks. It works by reducing inflammation and the buildup of uric acid crystals in the joints.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Gout": "Avoid trigger foods high in purines (red meat, organ meats, certain seafood), limit alcohol (especially beer), stay hydrated, and rest the affected joint."
        },
        "notes": "Prescription-only. Can have significant gastrointestinal side effects (nausea, diarrhea). Has a narrow therapeutic window, and overdose can be very dangerous."
    },
    "cyclobenzaprine": {
        "description": "A skeletal muscle relaxant used for the short-term relief of muscle spasms and pain associated with acute musculoskeletal conditions.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Muscle Spasms": "Rest, ice/heat therapy, gentle stretching, and physical therapy."
        },
        "notes": "Prescription-only. A very common side effect is drowsiness, which can impair driving and other activities. Should only be used for short periods (2-3 weeks)."
    },
    "diclofenac": {
        "description": "A nonsteroidal anti-inflammatory drug (NSAID) used to treat pain, inflammation, and arthritis. Available in oral and topical forms.",
        "alternatives": [
            "Ibuprofen",
            "Naproxen",
            "Celecoxib"
        ],
        "home_remedies_for_common_uses": {
            "For Pain/Inflammation": "Rest, ice, compression, elevation (RICE). Physical therapy."
        },
        "notes": "Available by prescription and in lower-strength topical forms over-the-counter. Carries similar risks of gastrointestinal and cardiovascular side effects as other NSAIDs."
    },
    "gabapentin": {
        "description": "An anticonvulsant medication also used to treat neuropathic (nerve) pain, such as postherpetic neuralgia (shingles pain) and diabetic neuropathy.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Nerve Pain": "Gentle exercise, physical therapy, mindfulness and meditation to manage the mental aspect of chronic pain, warm compresses."
        },
        "notes": "Prescription-only. Common side effects include dizziness and drowsiness. The dose is usually started low and increased gradually. Can have potential for misuse and dependence."
    },
    "meloxicam": {
        "description": "A nonsteroidal anti-inflammatory drug (NSAID) used to treat pain and inflammation from osteoarthritis and rheumatoid arthritis.",
        "alternatives": [
            "Naproxen",
            "Ibuprofen",
            "Celecoxib"
        ],
        "home_remedies_for_common_uses": {
            "For Arthritis": "Weight management, low-impact exercise, physical therapy, application of heat or cold."
        },
        "notes": "Prescription-only. It is longer-acting than ibuprofen, allowing for once-daily dosing. Carries the same cardiovascular and gastrointestinal risks as other NSAIDs."
    },
    "methocarbamol": {
        "description": "A central nervous system depressant used as a skeletal muscle relaxant to treat muscle spasms and pain.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Muscle Pain": "Rest, physical therapy, massage, and application of heat or ice."
        },
        "notes": "Prescription-only. Can cause drowsiness, dizziness, and lightheadedness. May turn urine brown, black, or green, which is a harmless side effect."
    },
    "oxycodone": {
        "description": "A potent opioid analgesic used for the management of moderate to severe pain.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Pain Management": "Non-pharmacological approaches like physical therapy, acupuncture, massage, and cognitive-behavioral therapy can be used as part of a comprehensive pain management plan."
        },
        "notes": "Prescription-only, Schedule II controlled substance. High potential for addiction, abuse, and misuse. Side effects include constipation, drowsiness, and respiratory depression. Should be used with extreme caution."
    },
    "prednisone": {
        "description": "A systemic corticosteroid used to treat a wide variety of inflammatory and autoimmune conditions, such as severe allergies, asthma, arthritis, and lupus.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "General Support for Inflammation": "An anti-inflammatory diet, stress management, and adequate rest can support overall health during treatment."
        },
        "notes": "Prescription-only. Long-term use can cause significant side effects, including weight gain, mood swings, osteoporosis, and increased risk of infection. The dose must be tapered off slowly, not stopped abruptly."
    },
    "pregabalin": {
        "description": "An anticonvulsant and gabapentinoid used to treat nerve pain, fibromyalgia, seizures, and generalized anxiety disorder.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Nerve Pain/Fibromyalgia": "Graded exercise therapy, stress-reduction techniques like yoga and meditation, maintaining a regular sleep schedule."
        },
        "notes": "Prescription-only. Common side effects include dizziness, drowsiness, and weight gain. Can have potential for misuse and dependence."
    },
    "tizanidine": {
        "description": "A short-acting muscle relaxant (an alpha-2 adrenergic agonist) used to treat muscle spasticity.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Muscle Spasticity": "Stretching exercises, physical therapy, and occupational therapy."
        },
        "notes": "Prescription-only. Can cause significant drowsiness, dizziness, and dry mouth. It is short-acting and typically dosed multiple times per day."
    },
    "tramadol": {
        "description": "A centrally-acting opioid analgesic used to treat moderate to moderately severe pain.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Pain": "Physical therapy, ice/heat application, and mindfulness techniques can complement medication."
        },
        "notes": "Prescription-only, Schedule IV controlled substance. Carries a risk of addiction and dependence. Can lower the seizure threshold and has a risk of serotonin syndrome when combined with other serotonergic drugs."
    },
    "chlorphenamine": {
        "description": "A first-generation antihistamine used to relieve symptoms of allergies and the common cold.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Cold/Allergy Symptoms": "Rest, hydration, saline nasal sprays, and using a humidifier."
        },
        "notes": "Commonly causes significant drowsiness and is often used in nighttime cold and allergy formulations. Anticholinergic side effects like dry mouth are also common."
    },
    "bismuth_subsalicylate": {
        "description": "An antidiarrheal and antacid used to treat diarrhea, heartburn, nausea, and upset stomach.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Diarrhea": "Stay hydrated with clear fluids or oral rehydration solutions. Follow the BRAT diet (bananas, rice, applesauce, toast)."
        },
        "notes": "Can cause a harmless darkening of the stool and tongue. Contains salicylate; should not be given to children or teenagers recovering from viral infections due to the risk of Reye's syndrome."
    },
    "esomeprazole": {
        "description": "A proton pump inhibitor (PPI) that reduces stomach acid. Used to treat GERD, ulcers, and other acid-related conditions.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Acid Reflux": "Avoid trigger foods, eat smaller meals, don't lie down after eating, and elevate the head of the bed."
        },
        "notes": "Chemically very similar to omeprazole. Should be taken on an empty stomach before a meal. Long-term use carries risks like vitamin B12 deficiency and bone fractures."
    },
    "famotidine": {
        "description": "A histamine-2 (H2) blocker that reduces the amount of acid produced by the stomach. Used for GERD, ulcers, and heartburn.",
        "alternatives": [
            "Proton Pump Inhibitors (Omeprazole, for more potent and longer-lasting suppression)",
            "Antacids (for immediate relief)"
        ],
        "home_remedies_for_common_uses": {
            "For Heartburn": "Dietary modifications, avoiding late-night meals, and weight management."
        },
        "notes": "Works faster than PPIs but is less potent and has a shorter duration of action. Available over-the-counter and by prescription."
    },
    "lansoprazole": {
        "description": "A proton pump inhibitor (PPI) used to treat and prevent stomach and intestinal ulcers, erosive esophagitis, and other conditions involving excessive stomach acid.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For GERD": "Lifestyle changes such as diet modification, weight loss, and avoiding triggers."
        },
        "notes": "Should be taken before a meal. Long-term use is associated with an increased risk of bone fractures and vitamin B12 deficiency."
    },
    "loperamide": {
        "description": "An antidiarrheal agent used to decrease the frequency of diarrhea by slowing down intestinal movement.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Diarrhea": "Crucial to stay hydrated with water, broths, or oral rehydration solutions. The BRAT diet (bananas, rice, applesauce, toast) can help firm up stools."
        },
        "notes": "Should not be used if there is fever or bloody/black stool, as it can worsen certain infections. Overuse can lead to serious heart problems."
    },
    "metoclopramide": {
        "description": "A prokinetic agent and antiemetic used to treat GERD, nausea, and gastroparesis (delayed stomach emptying).",
        "alternatives": [
            "Ondansetron (for nausea)",
            "Erythromycin (for gastroparesis)"
        ],
        "home_remedies_for_common_uses": {
            "For Nausea/Gastroparesis": "Eating small, frequent meals that are low in fat and fiber. Avoiding carbonated beverages."
        },
        "notes": "Prescription-only. Carries a boxed warning for the risk of tardive dyskinesia (a serious, often irreversible movement disorder) with long-term or high-dose use."
    },
    "pantoprazole": {
        "description": "A proton pump inhibitor (PPI) that decreases the amount of acid produced in the stomach, used for GERD and erosive esophagitis.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Acid Reflux": "Dietary and lifestyle adjustments, such as avoiding trigger foods and eating smaller meals."
        },
        "notes": "Prescription-only. Like other PPIs, it is associated with risks of bone fracture and vitamin B12 deficiency with long-term use."
    },
    "sucralfate": {
        "description": "A mucosal protectant used to treat and prevent ulcers. It works by forming a protective barrier over the ulcer against acid and enzymes.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Ulcers": "Avoid smoking, alcohol, and NSAIDs. Manage stress."
        },
        "notes": "Prescription-only. The most common side effect is constipation. It can interfere with the absorption of many other medications and should be taken at a different time."
    },
    "benazepril": {
        "description": "An angiotensin-converting enzyme (ACE) inhibitor used to treat high blood pressure and heart failure.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Hypertension": "A low-sodium diet, regular exercise, and weight management."
        },
        "notes": "Prescription-only. Can cause a dry, persistent cough. Contraindicated in pregnancy."
    },
    "hydrochlorothiazide": {
        "description": "A thiazide diuretic ('water pill') used to treat high blood pressure and edema (fluid retention).",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Edema/Hypertension": "Reducing sodium intake is very effective in conjunction with this medication."
        },
        "notes": "Prescription-only. Can cause increased urination and may affect potassium and sodium levels, requiring monitoring. Increases sun sensitivity."
    },
    "valsartan": {
        "description": "An angiotensin II receptor blocker (ARB) used to treat high blood pressure and heart failure.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Hypertension": "Lifestyle modifications including diet (low sodium), exercise, and stress reduction."
        },
        "notes": "Prescription-only. Considered an alternative to ACE inhibitors for patients who cannot tolerate the cough. Contraindicated in pregnancy."
    },
    "glipizide": {
        "description": "A sulfonylurea drug used to control high blood sugar in people with type 2 diabetes. It works by stimulating the pancreas to release insulin.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Type 2 Diabetes": "Diet and exercise are essential components of management."
        },
        "notes": "Prescription-only. Carries a risk of hypoglycemia (low blood sugar). Can cause weight gain."
    },
    "glyburide": {
        "description": "A sulfonylurea drug used to treat type 2 diabetes by stimulating insulin release from the pancreas.",
        "alternatives": [
            "Metformin",
            "Glipizide",
            "GLP-1 agonists (Liraglutide)"
        ],
        "home_remedies_for_common_uses": {
            "For Type 2 Diabetes": "A consistent diet and regular physical activity are crucial for blood sugar control."
        },
        "notes": "Prescription-only. Higher risk of hypoglycemia compared to some other diabetes medications. Can cause weight gain."
    },
    "liraglutide": {
        "description": "A GLP-1 receptor agonist, administered by injection, used to treat type 2 diabetes and, at a higher dose, for weight management.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Diabetes/Weight Management": "Must be used in conjunction with a reduced-calorie diet and increased physical activity."
        },
        "notes": "Prescription-only. Common side effects are gastrointestinal (nausea, diarrhea). Carries a boxed warning for the risk of thyroid C-cell tumors."
    },
    "semaglutide": {
        "description": "A GLP-1 receptor agonist used to treat type 2 diabetes and for chronic weight management. Available as a weekly injection or a daily oral tablet.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Diabetes/Weight Management": "A healthy diet and regular exercise are necessary for the medication to be effective."
        },
        "notes": "Prescription-only. Gastrointestinal side effects are common. Carries a boxed warning for the risk of thyroid C-cell tumors."
    },
    "sitagliptin": {
        "description": "A DPP-4 inhibitor used to treat type 2 diabetes. It works by increasing levels of incretin hormones, which help control blood sugar.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Type 2 Diabetes": "Diet and exercise are fundamental to treatment."
        },
        "notes": "Prescription-only. Generally well-tolerated with a low risk of hypoglycemia. Has been associated with a risk of pancreatitis and severe joint pain."
    },
    "amitriptyline": {
        "description": "A tricyclic antidepressant (TCA) used to treat depression. It is also used off-label at lower doses for nerve pain and migraine prevention.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Depression/Pain": "Psychotherapy, exercise, and stress management techniques."
        },
        "notes": "Prescription-only. Has significant side effects, including drowsiness, dry mouth, and constipation, which are more pronounced than with newer antidepressants."
    },
    "aripiprazole": {
        "description": "An atypical antipsychotic used to treat schizophrenia, bipolar disorder, and as an add-on treatment for depression.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "General Support for Mental Health": "Therapy, support groups, and a structured daily routine."
        },
        "notes": "Prescription-only. Carries a boxed warning for increased mortality in elderly patients with dementia-related psychosis and for suicidal thoughts in younger patients."
    },
    "bupropion": {
        "description": "An atypical antidepressant also used for smoking cessation. It works by affecting the neurotransmitters norepinephrine and dopamine.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Depression": "Cognitive-behavioral therapy, exercise, and mindfulness.",
            "For Smoking Cessation": "Behavioral counseling and support groups."
        },
        "notes": "Prescription-only. Less likely to cause sexual side effects compared to SSRIs. Lowers the seizure threshold and should not be used in patients with a history of seizures or eating disorders."
    },
    "buspirone": {
        "description": "A non-benzodiazepine anxiolytic used for the treatment of generalized anxiety disorder (GAD).",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Anxiety": "Therapy (CBT), meditation, deep breathing exercises, and regular physical activity."
        },
        "notes": "Prescription-only. Does not cause dependence or withdrawal like benzodiazepines, but it takes several weeks to become fully effective. Common side effects include dizziness and nausea."
    },
    "citalopram": {
        "description": "A selective serotonin reuptake inhibitor (SSRI) used to treat depression.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Depression": "Psychotherapy, exercise, and maintaining a healthy lifestyle."
        },
        "notes": "Prescription-only. Carries a risk of dose-dependent QT prolongation (a heart rhythm issue), so doses are often limited, especially in older adults."
    },
    "clonazepam": {
        "description": "A long-acting benzodiazepine used to treat seizures, panic disorder, and anxiety.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Anxiety": "Stress management techniques and therapy."
        },
        "notes": "Prescription-only, Schedule IV controlled substance. Carries risks of dependence, tolerance, and withdrawal. Its long half-life can lead to next-day drowsiness."
    },
    "diazepam": {
        "description": "A long-acting benzodiazepine used to treat anxiety, seizures, muscle spasms, and symptoms of alcohol withdrawal.",
        "alternatives": [
            "Other benzodiazepines (Clonazepam, Lorazepam)",
            "Muscle relaxants (Cyclobenzaprine) for spasms"
        ],
        "home_remedies_for_common_uses": {
            "For Anxiety/Muscle Spasms": "Relaxation techniques, physical therapy."
        },
        "notes": "Prescription-only, Schedule IV controlled substance. High potential for dependence. Long half-life can cause accumulation and prolonged sedation, especially in the elderly."
    },
    "duloxetine": {
        "description": "A serotonin-norepinephrine reuptake inhibitor (SNRI) used to treat depression, anxiety, nerve pain, and fibromyalgia.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Depression/Pain": "A combination of medication with therapy, physical activity, and stress reduction is most effective."
        },
        "notes": "Prescription-only. Can cause nausea, dry mouth, and fatigue. Discontinuation should be done gradually to avoid withdrawal symptoms."
    },
    "escitalopram": {
        "description": "A selective serotonin reuptake inhibitor (SSRI) used to treat depression and generalized anxiety disorder.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Depression/Anxiety": "Therapy (CBT), mindfulness, exercise, and a stable routine."
        },
        "notes": "Prescription-only. Often considered to have fewer side effects than other SSRIs. Like others in its class, it can take several weeks to work fully."
    },
    "lamotrigine": {
        "description": "An anticonvulsant medication also used as a mood stabilizer in bipolar disorder.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "General Support for Bipolar/Epilepsy": "Maintaining a regular sleep schedule, managing stress, and avoiding alcohol and recreational drugs."
        },
        "notes": "Prescription-only. Requires a very slow dose titration when starting to reduce the risk of a serious, potentially life-threatening skin rash (Stevens-Johnson syndrome)."
    },
    "levetiracetam": {
        "description": "An anticonvulsant medication used to treat various types of seizures.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Epilepsy": "Ensuring adequate sleep, managing stress, and avoiding known seizure triggers (like flashing lights for some individuals)."
        },
        "notes": "Prescription-only. Generally well-tolerated but can cause behavioral side effects like irritability, agitation, and mood swings."
    },
    "lorazepam": {
        "description": "An intermediate-acting benzodiazepine used to treat anxiety, insomnia, and seizures.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Anxiety/Insomnia": "Cognitive-behavioral therapy for insomnia (CBT-I), relaxation techniques, and good sleep hygiene."
        },
        "notes": "Prescription-only, Schedule IV controlled substance. Carries risks of dependence, tolerance, and withdrawal. Often used in hospital settings for sedation."
    },
    "olanzapine": {
        "description": "An atypical antipsychotic used to treat schizophrenia and bipolar disorder.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "General Support for Mental Health": "A supportive environment, therapy, and a consistent daily routine."
        },
        "notes": "Prescription-only. Associated with significant metabolic side effects, including weight gain, high blood sugar, and high cholesterol, requiring regular monitoring."
    },
    "topiramate": {
        "description": "An anticonvulsant medication also used for migraine prevention and sometimes for weight loss in combination with another drug.",
        "alternatives": [
            "Other anticonvulsants (for seizures)",
            "Other migraine preventatives (Propranolol, Amitriptyline)"
        ],
        "home_remedies_for_common_uses": {
            "For Migraines": "Identifying and avoiding triggers, maintaining a regular sleep and meal schedule, and stress management."
        },
        "notes": "Prescription-only. Common side effects include cognitive issues ('brain fog'), tingling in extremities, and kidney stones. Requires slow dose titration."
    },
    "bacitracin": {
        "description": "A polypeptide antibiotic used topically to prevent minor skin infections in cuts, scrapes, and burns.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "For Minor Wounds": "Clean the wound thoroughly with soap and water, apply the antibiotic, and cover with a sterile bandage."
        },
        "notes": "Available over-the-counter. Contact dermatitis (allergic skin reaction) is a potential side effect."
    },
    "cephalexin": {
        "description": "A first-generation cephalosporin antibiotic used to treat a variety of bacterial infections, particularly skin and soft tissue infections.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "General Support for Infections": "Rest, hydration, and completing the full course of medication."
        },
        "notes": "Prescription-only. Generally well-tolerated. Patients with a severe penicillin allergy may also be allergic to cephalosporins."
    },
    "clindamycin": {
        "description": "A lincosamide antibiotic used to treat a wide range of serious bacterial infections, including skin, lung, and internal organ infections.",
        "alternatives":[],
        "home_remedies_for_common_uses": {
            "General Support for Infections": "Adequate rest and fluid intake."
        },
        "notes": "Prescription-only. Carries a boxed warning for a high risk of causing Clostridioides difficile-associated diarrhea, which can be severe."
    },
    "doxycycline": {
        "description": "A tetracycline antibiotic used to treat bacterial infections, malaria, acne, and rosacea.",
        "alternatives": [
            "Minocycline (for acne)",
            "Azithromycin (for respiratory infections)",
            "Amoxicillin"
        ],
        "home_remedies_for_common_uses": {
            "For Acne": "A consistent skincare routine with gentle cleansers and non-comedogenic moisturizers."
        },
        "notes": "Prescription-only. Should be taken with a full glass of water and the patient should remain upright for at least 30 minutes to prevent esophageal irritation. Causes significant sun sensitivity. Not recommended for children under 8 or pregnant women."
    },
    "metronidazole": {
        "description": "A nitroimidazole antibiotic and antiprotozoal used to treat bacterial and protozoal infections, such as C. difficile, bacterial vaginosis, and giardiasis.",
        "alternatives": [
            "Vancomycin (for C. difficile)",
            "Clindamycin (for bacterial vaginosis)"
        ],
        "home_remedies_for_common_uses": {
            "General Support for Infections": "Completing the full course of medication."
        },
        "notes": "Prescription-only. Alcohol must be strictly avoided during treatment and for at least 3 days after, as it can cause a severe reaction (nausea, vomiting, flushing). Can cause a metallic taste in the mouth."
    },
    "terbinafine": {
        "description": "An allylamine antifungal used to treat fungal infections of the skin (athlete's foot, ringworm) and nails. Available as a topical (OTC) and oral tablet (prescription).",
        "alternatives": [
            "Clotrimazole or Miconazole (topical)",
            "Itraconazole or Fluconazole (oral, for nail fungus)"
        ],
        "home_remedies_for_common_uses": {
            "For Fungal Infections": "Keep skin clean and dry, wear breathable footwear and clean socks."
        },
        "notes": "Oral terbinafine can cause liver problems and requires monitoring. It can also cause disturbances in taste and smell."
        }
    }
    return ALTERNATIVE_KNOWLEDGE_BASE