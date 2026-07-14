import pandas as pd
import joblib
import os

# ---------------------------------------------------------
# Load Dataset
# ---------------------------------------------------------

def load_dataset():

    path = "data/insurance_data_cleaned.csv"

    if os.path.exists(path):

        return pd.read_csv(path)

    return None


# ---------------------------------------------------------
# Load Premium Model
# ---------------------------------------------------------

def load_premium_model():

    path = "models/premium_model.pkl"

    if os.path.exists(path):

        return joblib.load(path)

    return None


# ---------------------------------------------------------
# Load Claim Model
# ---------------------------------------------------------

def load_claim_model():

    path = "models/claim_model.pkl"

    if os.path.exists(path):

        return joblib.load(path)

    return None


# ---------------------------------------------------------
# Predict Premium
# ---------------------------------------------------------

def predict_premium(model, input_df):

    prediction = model.predict(input_df)

    return round(float(prediction[0]),2)


# ---------------------------------------------------------
# Predict Claim
# ---------------------------------------------------------

def predict_claim(model, input_df):

    prediction = model.predict(input_df)[0]

    probability = None

    if hasattr(model,"predict_proba"):

        probability = model.predict_proba(input_df)[0][1]

    return prediction, probability


# ---------------------------------------------------------
# Risk Level
# ---------------------------------------------------------

def risk_level(probability):

    if probability is None:

        return "Unknown"

    probability = probability*100

    if probability < 30:

        return "Low"

    elif probability < 70:

        return "Medium"

    else:

        return "High"
