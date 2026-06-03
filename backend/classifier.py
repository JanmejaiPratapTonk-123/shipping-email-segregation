import joblib

model = joblib.load("../models/email_classifier.pkl")


def classify_email(text):

    prediction = model.predict([text])[0]

    probabilities = model.predict_proba([text])[0]

    confidence = max(probabilities)

    return {
        "category": prediction,
        "confidence": round(float(confidence), 4)
    }