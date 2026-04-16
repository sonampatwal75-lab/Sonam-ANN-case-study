import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("../model.pkl", "rb"))

st.title("Customer Churn Prediction")

age = st.slider("Age", 18, 60)
tenure = st.slider("Tenure Months", 1, 72)
monthly = st.number_input("Monthly Charges")

if st.button("Predict"):
    input_data = np.array([[1, age, tenure, 0, monthly, 1000, 1, 2, 1]])
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("Customer likely to churn")
    else:
        st.success("Customer likely to stay")