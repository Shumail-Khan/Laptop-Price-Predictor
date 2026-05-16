import os
import joblib
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

EUR_TO_PKR = float(os.getenv("EUR_TO_PKR", 320))

MODEL_PATH = "model/laptop_price_model.pkl"

model = joblib.load(MODEL_PATH)

def predict_price(data: dict):

    df = pd.DataFrame([data])

    pred_eur = model.predict(df)[0]

    pred_pkr = pred_eur * EUR_TO_PKR

    return {
        "price_eur": round(pred_eur, 2),
        "price_pkr": round(pred_pkr, 2)
    }