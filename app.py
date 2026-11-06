

import streamlit as st
import joblib

# Load trained model
model = joblib.load("spam_rf_pipeline.pkl")

# Page configuration
st.set_page_config(
    page_title="SMS Spam Detection",
    page_icon="📩",
    layout="centered"
)

st.title("📩 SMS Spam Detection")
st.write("Random Forest Machine Learning Model")

st.markdown("---")

message = st.text_area(
    "Enter your SMS Message:",
    placeholder="Type your message here..."
)

if st.button("Predict Message"):

    if message.strip() == "":
        st.warning("Please enter a message.")

    else:
        prediction = model.predict([message])[0]

        if prediction == 1:
            st.error("🚨 SPAM MESSAGE DETECTED!")
        else:
            st.success("✅ NORMAL (HAM) MESSAGE")

st.markdown("---")
st.caption("Powered by Random Forest Classifier")
