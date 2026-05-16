from fastapi import FastAPI
from sqlalchemy.orm import Session

from .schemas import LaptopInput
from .predict import predict_price
from .database import SessionLocal, engine
from .models import Base, Prediction

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Laptop Price Predictor API")

@app.get("/")
def root():
    return {"message": "Laptop Price Predictor API"}

@app.post("/predict")
def predict(data: LaptopInput):

    result = predict_price(data.dict())

    db: Session = SessionLocal()

    prediction = Prediction(
        company=data.Company,
        product=data.Product,
        ram=data.Ram,
        predicted_price_eur=result["price_eur"],
        predicted_price_pkr=result["price_pkr"]
    )

    db.add(prediction)
    db.commit()
    db.close()

    return result