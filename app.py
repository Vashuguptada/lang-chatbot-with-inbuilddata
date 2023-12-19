# type: ignore
import streamlit as st

from utils import get_answer_csv

# Provide the path to the predefined CSV file
predefined_csv_path = "sale.csv"

st.header("Chat with any CSV")
# Load the predefined CSV file
uploaded_file = open(predefined_csv_path, "rb")

query = st.text_area("Ask any question related to the document")
button = st.button("Submit")

if button:
    st.write(get_answer_csv(uploaded_file, query))

# uploaded_file = st.file_uploader("Upload a csv file", type=["csv"])

# if uploaded_file is not None:
#     query = st.text_area("Ask any question related to the document")
#     button = st.button("Submit")
#     if button:
#         st.write(get_answer_csv(uploaded_file, query))
