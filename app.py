import streamlit as st
import numpy as np
import joblib

model = joblib.load("rf_model.pkl")

st.title("Laptop Price Predictor")

st.divider()

st.write("With this app, you can get a price estimation of the laptop with the entered specifications. ")

st.divider()

processor_speed = st.number_input("Enter preferred processor speed in GHz", value = 2.50, step = 0.50)
ram_size = st.number_input("Enter preferred RAM size in GB", value = 16, step = 4)
storage_capacity = st.number_input("Enter preferred storage capacity in GB", value = 512, step = 256)

X = [processor_speed, ram_size, storage_capacity]

st.divider()

prediction = st.button("Price Estimation")

st.divider()

if prediction:
    st.balloons()
    x1 = np.array(X)
    prediction = model.predict([x1])[0]

    st.write(f"Price estimation for the laptop is {float(prediction):,.2f}")


else:
    st.write("Please press the button to get a prediction.")