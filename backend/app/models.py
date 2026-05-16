from sqlalchemy import Column, Integer, Float, String
from .database import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    company = Column(String)
    product = Column(String)
    ram = Column(Integer)

    predicted_price_eur = Column(Float)
    predicted_price_pkr = Column(Float)