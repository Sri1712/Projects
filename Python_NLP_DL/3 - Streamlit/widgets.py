import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 0, 100, 0)

if name:
    st.write(f"Hello, {name}!")
st.write(f"Your age is: {age}")

options = ["Python", "JavaScript", "C++", "Java"]
choice = st.selectbox("Select your favorite programming language:", options)
st.write(f"You selected: {choice}")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    uploaded_df = pd.read_csv(uploaded_file)
    st.write(uploaded_df)