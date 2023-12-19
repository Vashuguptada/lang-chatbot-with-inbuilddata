# app.py
# type: ignore
import streamlit as st
from utils import get_answer_csv

st.header("Chat with any CSV")

# Specify the path to the CSV file
csv_path = "sale.csv"

query = st.text_area("Ask any question related to the document")
button = st.button("Submit")

if button:
    st.write(get_answer_csv(csv_path, query))
