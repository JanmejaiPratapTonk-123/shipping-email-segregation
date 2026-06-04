from fastapi import FastAPI
from pydantic import BaseModel

from classifier import classify_email

from extractors.tonnage import extract_tonnage
from extractors.cargo_vc import extract_vc
from extractors.cargo_tc import extract_tc

app = FastAPI()


class EmailRequest(BaseModel):
    text: str


@app.post("/analyze")
def analyze_email(request: EmailRequest):

    text = request.text

    categories = classify_email(text)

    extracted = {}

    if "TONNAGE" in categories:
        extracted["TONNAGE"] = extract_tonnage(text)

    if "CARGO_VC" in categories:
        extracted["CARGO_VC"] = extract_vc(text)

    if "CARGO_TC" in categories:
        extracted["CARGO_TC"] = extract_tc(text)

    return {
        "categories": categories,
        "extracted_data": extracted
    }