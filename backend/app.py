from fastapi import FastAPI
from pydantic import BaseModel

from backend.extractors.tonnage import extract_tonnage
from backend.extractors.cargo_vc import extract_cargo_vc
from backend.extractors.cargo_tc import extract_cargo_tc

app = FastAPI()


class EmailRequest(BaseModel):
    email_text: str


@app.get("/")
def home():
    return {"message": "Shipping Email Segregation API Running"}


@app.post("/analyze")
def analyze_email(request: EmailRequest):

    email_text = request.email_text
    text = email_text.lower()

    categories = []

    # TONNAGE
    if any(word in text for word in [
        "dwt",
        "open vessel",
        "mv ",
        "open "
    ]):
        categories.append("TONNAGE")

    # CARGO VC
    if any(word in text for word in [
        "load port",
        "loading port",
        "discharge port"
    ]):
        categories.append("CARGO_VC")

    # CARGO TC
    if any(word in text for word in [
        "delivery port",
        "redelivery port",
        "duration"
    ]):
        categories.append("CARGO_TC")

    extracted_data = {}

    if "TONNAGE" in categories:
        extracted_data["TONNAGE"] = extract_tonnage(email_text)

    if "CARGO_VC" in categories:
        extracted_data["CARGO_VC"] = extract_cargo_vc(email_text)

    if "CARGO_TC" in categories:
        extracted_data["CARGO_TC"] = extract_cargo_tc(email_text)

    return {
        "categories": categories,
        "extracted_data": extracted_data
    }