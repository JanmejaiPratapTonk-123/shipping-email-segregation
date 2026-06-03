# Shipping Email Segregation & Data Extraction System

## Overview

This project automatically classifies shipping emails into different business categories and extracts structured commercial information for further processing.

The system is developed without using external Large Language Model APIs such as OpenAI or Claude.

---

# Features

## Email Classification

The system classifies emails into:

* TONNAGE
* CARGO_VC
* CARGO_TC

---

## Information Extraction

### Tonnage Emails

Extracted fields:

* Vessel Name
* Account Name
* Open Port
* Open Date
* Vessel Type
* Vessel Size

### Cargo VC Emails

Extracted fields:

* Account Name
* Cargo Name
* Loading Port
* Discharge Port
* Laycan
* Cargo Type

### Cargo TC Emails

Extracted fields:

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

---

# System Architecture

Shipping Email
→ ML Classification
→ Category Detection
→ Information Extraction
→ Structured JSON Output

---

# Project Structure

```text
backend/
    app.py
    classifier.py
    train.py
    extractors/

frontend/
    app.py

dataset/
models/
```

---

# Machine Learning Approach

The project uses:

* TF-IDF vectorization for text feature extraction
* Logistic Regression for classification

Regex-based extraction is used for structured information retrieval from shipping emails.

---

# How to Run

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Backend

```bash
cd backend
uvicorn app:app --reload
```

## Run Frontend

```bash
cd frontend
streamlit run app.py
```

---

# Sample Output

The system returns:

* Email category
* Confidence score
* Extracted structured data

---

# Future Scope

* Vessel-to-cargo matching
* Duplicate email detection
* Broker/customer analytics
* Market opportunity alerts
* Database integration