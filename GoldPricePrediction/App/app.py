import streamlit as st
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
from sklearn.model_selection import train_test_split
st.sidebar.header("Select the parameters")

def define_sidebar():
    SPX = st.sidebar.slider("SPX",676.53,2872.87,900.00)
    USO = st.sidebar.slider("USO",7.96, 117.48, 50.00)
    SLV = st.sidebar.slider("SLV",8.85, 47.25, 20.00)
    EURUSD = st.sidebar.slider("EUR/USD",1.039, 1.598, 1.400)
    YEAR = st.sidebar.slider("YEAR",2008.00, 2018.00, 2014.00)
    MONTH = st.sidebar.slider("MONTH",8.85, 1.00, 12.00)
    DAY = st.sidebar.slider("DAY",1.00,31.00)
    features=pd.DataFrame({
        "SPX":SPX,
        "USO":USO,
        "SLV":SLV,
        "EURUSD": EURUSD,
        "YEAR": YEAR,
        "MONTH": MONTH,
        "DAY":DAY
    },index=[0])
    return features
st.title("Gold price prediction")
df = define_sidebar()
st.subheader("User input parameters")
st.write(df)
model = pickle.load(open('model.pkl','rb'))

if st.button("Predict"):
    prediction = model.predict(df)
    st.write(prediction)



