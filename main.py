import streamlit as st
import pickle
from preprocessing import clean_text
from alert import send_alert_email

# Load saved model and vectorizer
with open('spam_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

st.title("Spam Message Detector")

msg = st.text_area("Enter your message:")

if st.button("Check"):
    clean_msg = clean_text(msg)
    vector = vectorizer.transform([clean_msg])
    prediction = model.predict(vector)
    result = "Spam" if prediction[0] == 1 else "Ham (Not Spam)"
    st.subheader(result)

    if prediction[0] == 1:
        send_alert_email(msg)