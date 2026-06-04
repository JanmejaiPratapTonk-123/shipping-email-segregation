# Shipping Email Segregation & Data Extraction System

## Live Demo

Live Application:
https://shipping-email-segregation.streamlit.app/

GitHub Repository:
https://github.com/JanmejaiPratapTonk-123/shipping-email-segregation

---

# Overview

The Shipping Email Segregation & Data Extraction System is an AI/ML-based application developed to automate the processing of shipping and chartering emails.

The system reads shipping emails, classifies them into business categories, and extracts important commercial information in a structured format.

This project is developed without using any third-party Large Language Model (LLM) APIs such as OpenAI ChatGPT or Claude.

The solution uses:

* Machine Learning
* Natural Language Processing
* Regex-based Information Extraction
* Rule-based Multi-category Detection

---

# Objective

The goal of this project is to:

* Automatically classify shipping emails
* Extract structured business information
* Reduce manual data entry
* Improve operational efficiency
* Support vessel and cargo matching workflows

---

# Supported Email Categories

## 1. TONNAGE

Emails containing vessel availability information.

### Extracted Fields

* Vessel Name
* Account Name
* Open Port
* Open Date
* Vessel Type
* Vessel Size

---

## 2. CARGO_VC (Voyage Charter Cargo)

Emails containing voyage cargo requirements.

### Extracted Fields

* Account Name
* Cargo Name
* Loading Port
* Discharge Port
* Laycan
* Cargo Type

---

## 3. CARGO_TC (Time Charter Cargo)

Emails containing time charter cargo requirements.

### Extracted Fields

* Account Name
* Cargo Name
* Delivery Port
* Redelivery Port
* Duration
* Laycan
* Cargo Type

---

# Features

## Email Classification

The system automatically classifies incoming shipping emails into:

* TONNAGE
* CARGO_VC
* CARGO_TC

---

## Multi-Category Detection

The application supports emails containing multiple categories simultaneously.

Example:

* Vessel availability + cargo requirement in same email

---

## Information Extraction

The system extracts:

* vessel details
* cargo details
* ports
* dates
* charter information

and returns structured JSON output.

---

## Live Web Application

The project includes:

* FastAPI backend
* Streamlit frontend
* Public cloud deployment

---

# Technologies Used

## Backend

* Python
* FastAPI
* Scikit-learn
* Regex
* Joblib

## Frontend

* Streamlit

## Machine Learning

* TF-IDF Vectorization
* Logistic Regression

---

# Machine Learning Approach

## TF-IDF Vectorization

Email text is converted into numerical feature vectors using TF-IDF.

## Logistic Regression

A Logistic Regression classifier is trained on shipping email datasets for category prediction.

---

# Project Architecture

```text
Shipping Email
       ↓
Text Preprocessing
       ↓
ML Classification
       ↓
Category Detection
       ↓
Regex-based Extraction
       ↓
Structured JSON Output
```

---

# Project Structure

```text
shipping-email-segregation/

│
├── backend/
│   ├── app.py
│   ├── classifier.py
│   ├── train.py
│   └── extractors/
│       ├── tonnage.py
│       ├── cargo_vc.py
│       └── cargo_tc.py
│
├── frontend/
│   └── app.py
│
├── dataset/
│
├── models/
│   └── email_classifier.pkl
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# How to Run Locally

## 1. Clone Repository

```bash
git clone https://github.com/JanmejaiPratapTonk-123/shipping-email-segregation.git
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Run Backend

```bash
cd backend
uvicorn app:app --reload
```

---

## 4. Run Frontend

```bash
cd frontend
streamlit run app.py
```

---

# Sample Input

```text
From: broker@shipping.com
Subject: Open Vessel and Cargo Opportunity

MV BLUE STAR 38K DWT OPEN SINGAPORE ON 15 JULY.

AVAILABLE FOR COAL CARGO.

Cargo: 30000 MTS COAL
Load Port: INDIA
Discharge Port: CHINA
Laycan: 15 JULY

Regards,
Shipping Broker
```

---

# Sample Output

```json
{
  "categories": [
    "TONNAGE",
    "CARGO_VC"
  ],
  "extracted_data": {
    "TONNAGE": {
      "vessel_name": "BLUE STAR",
      "vessel_type": "Bulk Carrier",
      "vessel_size": "38K"
    },
    "CARGO_VC": {
      "cargo_name": "30000 MTS COAL",
      "loading_port": "INDIA",
      "discharge_port": "CHINA",
      "cargo_type": "Voyage Charter"
    }
  }
}
```

---

# Expected Outcome

* Automatic segregation of shipping emails
* Reduced manual effort
* Structured vessel and cargo database creation
* Faster business processing
* Improved operational visibility

---

# Future Scope

* Multiple vessel extraction
* Multiple cargo extraction
* Vessel-to-cargo matching
* Duplicate email detection
* Broker/customer analytics
* Database integration
* Market opportunity alerts

---

# Conclusion

This project demonstrates the use of Machine Learning and NLP techniques for automating shipping email processing.

The system successfully:

* classifies shipping emails
* extracts structured information
* handles multi-category edge cases
* generates business-ready JSON output

without relying on external AI APIs.
