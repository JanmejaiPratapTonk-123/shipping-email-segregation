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
            "http://127.0.0.1:8000/analyze",
            json={
                "text": email
            }
        )

        result = response.json()

        st.success("Analysis Completed")

        st.subheader("Categories")

        for cat in result["categories"]:
            st.write(cat)

        st.subheader("Extracted Data")

        st.json(result["extracted_data"])