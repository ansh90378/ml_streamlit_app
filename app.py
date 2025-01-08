import streamlit as st
import numpy as np
import joblib

# load trained model
model = joblib.load("model/model.pkl")

st.title("Iris Flower Prediction Model")

# input features
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.0)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 5.0, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.0)

# prepare input data
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# predict
prediction = model.predict(input_data)
predicted_class = {0: 'setosa', 1 : 'versicolor', 2 : 'virginica'}[prediction[0]]

# display result
st.write(f"Predicted Iris Species: **{predicted_class}**")





