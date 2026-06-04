# Shipping Email Segregation & Data Extraction System

## Overview

The Shipping Email Segregation & Data Extraction System is an AI/ML-based application developed to automate the processing of shipping and chartering emails.

The system reads incoming shipping emails, classifies them into relevant business categories, and extracts structured commercial information for further operational use.

This solution is developed without using any external Large Language Model (LLM) APIs such as OpenAI ChatGPT or Claude. The project uses Machine Learning, NLP techniques, and regex-based extraction methods.

---

# Problem Statement

Shipping companies and chartering teams receive hundreds of broker and cargo emails daily. Manual segregation and extraction of information from these emails is time-consuming and error-prone.

This project automates:

* Email categorization
* Information extraction
* Structured data generation
* Multi-category email handling

---

# Features

## Email Classification

The system classifies emails into:

* TONNAGE
* CARGO_VC
* CARGO_TC

The system also supports hybrid emails containing multiple categories.

Example:

```text
MV BLUE STAR 38K DWT OPEN SINGAPORE

Cargo: 30000 MTS COAL
Load Port: INDIA
Discharge Port: CHINA
Laycan: 15 JULY
```

Output:

```json
{
  "categories": [
    "TONNAGE",
    "CARGO_VC"
  ]
}
```

---

# Information Extraction

## Tonnage Emails

Extracted Fields:

* Vessel Name
* Account Name
* Open Port
* Open Date
* Vessel Type
* Vessel Size

---

## Cargo VC Emails

Extracted Fields:

* Account Name
* Cargo Name
* Loading Port
* Discharge Port
* Laycan
* Cargo Type

---

## Cargo TC Emails

Extracted Fields:

* Account Name
* Cargo Name
* Delivery Port
* Redelivery Port
* Duration
* Laycan
* Cargo Type

---

# Technologies Used

* Python
* FastAPI
* Streamlit
* Scikit-learn
* TF-IDF Vectorization
* Logistic Regression
* Regex-based NLP
* JSON Data Handling

---

# System Architecture

```text
Shipping Email
       ↓
Email Classification
       ↓
Category Detection
       ↓
Information Extraction
       ↓
Structured JSON Output
```

---

# Machine Learning Approach

The project uses:

## TF-IDF Vectorization

Used to convert email text into numerical feature vectors.

## Logistic Regression

Used for email category classification.

The model is trained on a custom shipping email dataset.

---

# Multi-Category Detection

An additional keyword-based detection layer is implemented to identify emails containing more than one shipping category.

This helps process real-world broker emails that may contain:

* vessel availability
* cargo requirements
* charter requests

inside the same message.

---

# Information Extraction Logic

Regex-based extraction methods are used for:

* vessel information
* cargo details
* loading/discharge ports
* laycan dates
* charter duration

The extraction logic is modular and separated into dedicated extractor files.

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

# How to Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
cd backend
uvicorn app:app --reload
```

---

## Run Frontend

```bash
cd frontend
streamlit run app.py
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
      "vessel_size": "38K"
    },
    "CARGO_VC": {
      "cargo_name": "30000 MTS COAL",
      "loading_port": "INDIA",
      "discharge_port": "CHINA"
    }
  }
}
```

---

# Expected Outcome

* Automatic segregation of shipping emails
* Elimination of manual data entry
* Faster cargo and vessel processing
* Structured shipping data generation
* Better operational efficiency

---

# Future Scope

* Vessel-to-cargo matching
* Duplicate email detection
* Broker/customer analytics
* Database integration
* Market opportunity alerts
* Voyage workflow integration

---

# Conclusion

This project demonstrates the use of Machine Learning and NLP techniques to automate shipping email processing.

The system successfully:

* classifies shipping emails
* extracts structured information
* supports multi-category edge cases
* generates usable JSON output

without relying on external AI APIs.