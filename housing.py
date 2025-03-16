import streamlit as st
import joblib
import numpy as np

model=joblib.load('house_price_prediction.pk1')

st.title('hose price prediction')

RM = st.number_input('RM',value=0.0)
LSTAT = st.number_input('LSTAT',value=0.0)
PTRATIO= st.number_input('PTRATIO',value=0.0)

if st.button("predict"):
    features=np.array([RM,LSTAT,PTRATIO]).reshape(1,-1)
    prediction = model.predict(features)
    st.success(f"Predicted Price: ${prediction[0]:,.2f}")
    