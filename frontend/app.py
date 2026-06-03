import streamlit as st
import requests

st.set_page_config(page_title="Shipping Email Segregation")

st.title("Shipping Email Segregation & Data Extraction")

email = st.text_area(
    "Paste Shipping Email",
    height=300
)

if st.button("Analyze Email"):

    if email.strip() == "":
        st.warning("Please enter email text")
    else:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json={
                "email": email
            }
        )

        result = response.json()

        st.success("Analysis Completed")

        st.subheader("Category")
        st.write(result["category"])

        st.subheader("Confidence")
        st.write(result["confidence"])

        st.subheader("Extracted Data")
        st.json(result["extracted_data"])