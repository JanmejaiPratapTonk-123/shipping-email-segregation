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

        try:

            response = requests.post(
                "https://shipping-email-segregation.onrender.com/analyze",
                json={
                    "email_text": email
                }
            )

            result = response.json()

            st.success("Analysis Completed")

            if "categories" in result:

                st.subheader("Categories")

                for cat in result["categories"]:
                    st.write(cat)

                st.subheader("Extracted Data")

                cleaned = {}

                for category, values in result["extracted_data"].items():

                    cleaned[category] = {
                        k: v for k, v in values.items()
                        if v not in [None, "", "NULL"]
                    }

                st.json(cleaned)

            else:
                st.error(result)

        except Exception as e:
            st.error(f"Error: {e}")