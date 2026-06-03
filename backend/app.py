from fastapi import FastAPI
from classifier import classify_email

from extractors.tonnage import extract_tonnage
from extractors.cargo_vc import extract_vc
from extractors.cargo_tc import extract_tc

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Shipping Email Segregation API Running"
    }


@app.post("/predict")
def predict(data: dict):

    email_text = data["email"]

    result = classify_email(email_text)

    category = result["category"]

    extracted_data = {}

    if category == "TONNAGE":
        extracted_data = extract_tonnage(email_text)

    elif category == "CARGO_VC":
        extracted_data = extract_vc(email_text)

    elif category == "CARGO_TC":
        extracted_data = extract_tc(email_text)

    return {
        "category": category,
        "confidence": result["confidence"],
        "extracted_data": extracted_data
    }