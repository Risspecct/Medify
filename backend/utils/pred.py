import pickle
import numpy as np
import os
import pandas as pd

# Load the assets once when the server starts
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'disease_model.pkl')
with open(model_path, 'rb') as f:
    assets = pickle.load(f)

model = assets["model"]
encoder = assets["encoder"]
symptom_list = assets["symptom_list"]

def predict(user_input_symptoms):
    
    # 1. Create a zero-vector based on the training features
    input_vector = np.zeros(len(symptom_list))
    
    # 2. Fill the vector with 1s for symptoms the user HAS
    for s in user_input_symptoms:
        if s in symptom_list:
            idx = symptom_list.index(s)
            input_vector[idx] = 1
            
    # 3. Predict Probabilities
    input_df = pd.DataFrame([input_vector], columns=symptom_list)
    probs = model.predict_proba(input_df)[0]
    
    # 4. Get Top 3
    top_3_idx = np.argsort(probs)[-3:][::-1]
    
    results = []
    for i in top_3_idx:
        p = probs[i]
        if p > 0.1: # Only include if it's at least 10% likely
            results.append({
                "disease": encoder.classes_[i],
                "probability": f"{p*100:.1f}%",
                "confidence": "High" if p > 0.7 else "Medium" if p > 0.4 else "Low"
            })
            
    return results