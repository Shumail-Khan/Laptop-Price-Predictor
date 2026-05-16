import streamlit as st
import requests

st.title("Laptop Price Predictor")

company = st.text_input("Company")
product = st.text_input("Product")
typename = st.text_input("Type")
inches = st.number_input("Inches")
screen = st.text_input("Screen Resolution")
cpu = st.text_input("CPU")
ram = st.number_input("RAM")
memory = st.text_input("Memory")
gpu = st.text_input("GPU")
osys = st.text_input("Operating System")
weight = st.number_input("Weight")

currency = st.selectbox(
    "Currency",
    ["EUR", "PKR"]
)

if st.button("Predict Price"):

    payload = {
        "Company": company,
        "Product": product,
        "TypeName": typename,
        "Inches": inches,
        "ScreenResolution": screen,
        "Cpu": cpu,
        "Ram": ram,
        "Memory": memory,
        "Gpu": gpu,
        "OpSys": osys,
        "Weight": weight
    }

    response = requests.post(
        "http://backend:8000/predict",
        json=payload
    )

    result = response.json()

    if currency == "EUR":
        st.success(f"Predicted Price: €{result['price_eur']}")

    else:
        st.success(f"Predicted Price: Rs {result['price_pkr']}")