import joblib

model = joblib.load("../models/email_classifier.pkl")


def classify_email(text):

    text_upper = text.upper()

    categories = []

    tonnage_keywords = [
        "MV",
        "OPEN",
        "DWT",
        "VESSEL"
    ]

    vc_keywords = [
        "LOAD PORT",
        "DISCHARGE PORT",
        "CARGO",
        "MTS"
    ]

    tc_keywords = [
        "DELIVERY",
        "REDELIVERY",
        "DURATION",
        "TIME CHARTER"
    ]

    if any(word in text_upper for word in tonnage_keywords):
        categories.append("TONNAGE")

    if any(word in text_upper for word in vc_keywords):
        categories.append("CARGO_VC")

    if any(word in text_upper for word in tc_keywords):
        categories.append("CARGO_TC")

    if len(categories) == 0:

        prediction = model.predict([text])[0]

        categories.append(prediction)

    return categories