import joblib
import pandas as pd

MODEL_PATH = "./laptop_price_model.pkl"
model = joblib.load(MODEL_PATH)

EUR_TO_PKR = 320  # later replace with API

def predict_price(input_data: dict, currency="EUR"):
    """
    input_data: dictionary of laptop features
    currency: 'EUR' or 'PKR'
    """

    # Convert input to DataFrame (required by sklearn pipeline)
    df = pd.DataFrame([input_data])

    # Predict (model already includes preprocessing pipeline)
    pred_eur = model.predict(df)[0]

    if currency.upper() == "PKR":
        return {
            "price_eur": float(pred_eur),
            "price_pkr": float(pred_eur * EUR_TO_PKR)
        }

    return {
        "price_eur": float(pred_eur)
    }


if __name__ == "__main__":
    sample = {
    "Company": "Apple",
    "Product": "MacBook Pro",
    "TypeName": "Ultrabook",
    "Inches": 13.3,
    "ScreenResolution": "IPS Panel Retina Display 2560x1600",
    "Cpu": "Intel Core i5",
    "Ram": 8,
    "Memory": 128,
    "Gpu": "Intel Iris Graphics",
    "OpSys": "macOS",
    "Weight": 1.37
}
    print(predict_price(sample, currency="PKR"))